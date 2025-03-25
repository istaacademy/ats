from django.urls import path
from course.api.views import *

urlpatterns = [
    path('course/register', CourseRegisterAPIView.as_view(), name='register-user'),
    path('course', CourseListAPIView.as_view(), name='course-list'),
    path('course/<int:pk>', CourseDetailAPIView.as_view(), name='course-detail'),
]