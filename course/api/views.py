from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from course.api.serializers import *
from rest_framework.permissions import IsAuthenticated



class CourseRegisterAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CourseRegisterSerializer
    def post(self, request):
        serializer = CourseRegisterSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyCourseListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CourseSerializer
    def get(self, request, user_id):
        objects = CourseUserModel.objects.filter(user__id=user_id).values_list("course", flat=True)
        courses = Course.objects.filter(id__in=list(objects))
        if courses.exists():
            serializer = CourseSerializer(courses, many=True)
            return Response({"data": serializer.data, "code": 200}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CourseListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CourseSerializer
    def get(self, request):
        courses = Course.objects.all()
        if courses:
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CourseDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CourseSerializer

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return None

    def get(self, request, pk):
        course = self.get_object(pk)
        if not course:
            return Response(data={"message":"Not found", "data": {}}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
