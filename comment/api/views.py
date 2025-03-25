# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from comment.models import Comment
from comment.api.serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class CommentCreateAPIView(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    def post(self, request):
        serializer = CommentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentListAPIView(APIView):
    serializer_class = CommentSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request):
        comments = Comment.objects.all()
        if comments:
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CommentDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return None

    def get(self, request, pk):
        comment = self.get_object(pk)
        if not comment:
            return Response(data={"message":"Not found", "data": {}}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)
        if not comment or comment.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        if not comment or comment.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)