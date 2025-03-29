from rest_framework.views import APIView
from utils.response_model import Result
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
            return Result.data(data=serializer.data, message="course created!")
        return Result.error(message=serializer.errors, code=status.HTTP_400_BAD_REQUEST)


class MyCourseListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CourseSerializer
    def get(self, request, user_id):
        objects = CourseUserModel.objects.filter(user__id=user_id).values_list("course", flat=True)
        courses = Course.objects.filter(id__in=list(objects))
        if courses.exists():
            serializer = CourseSerializer(courses, many=True)
            return Result.data(serializer.data, "get was successful!")
        else:
            return Result.error(message="no courses")


class CourseListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CourseSerializer
    def get(self, request):
        courses = Course.objects.all()
        if courses:
            serializer = CourseSerializer(courses, many=True)
            return Result.data(serializer.data, "get was successful!")
        else:
            return Result.error(message="no courses")

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
            return Result.error(message="no course")
        serializer = CourseSerializer(course)
        return Result.data(serializer.data, "get was successful!")
