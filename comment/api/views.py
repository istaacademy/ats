from rest_framework.views import APIView
from utils.response_model import Result
from rest_framework import status
from comment.models import Comment
from comment.api.serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated

class CommentCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer
    def post(self, request):
        serializer = CommentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Result.data(data=serializer.data, message="comment created!")
        return Result.error(message=serializer.errors, code=status.HTTP_400_BAD_REQUEST)


class CommentListAPIView(APIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        comments = Comment.objects.all()
        if comments:
            serializer = CommentSerializer(comments, many=True)
            return Result.data(data=serializer.data, message="get was successfully")
        else:
            return Result.error(message="no comments")

class CommentDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return None

    def get(self, request, pk):
        comment = self.get_object(pk)
        if not comment:
            return Result.error(message="Not found")
        serializer = CommentSerializer(comment)
        return Result.data(data=serializer.data, message="get was successfully")

    def put(self, request, pk):
        comment = self.get_object(pk)
        if not comment or comment.user != request.user:
            return Result.error(message="forbidden", code=status.HTTP_403_FORBIDDEN)

        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Result.data(serializer.data, message="get was successfully", code=status.HTTP_200_OK)
        return Result.error(message="Bad request", code=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        if not comment or comment.user != request.user:
            return Result.error(message="forbidden", code=status.HTTP_403_FORBIDDEN)

        comment.delete()
        return Result.data(message="deleted successfully", code=status.HTTP_204_NO_CONTENT)