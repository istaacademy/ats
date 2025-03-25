# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('comments/create', CommentCreateAPIView.as_view(), name='comment-create'),
    path('comments', CommentListAPIView.as_view(), name='comment-list'),
    path('comments/<int:pk>', CommentDetailAPIView.as_view(), name='comment-detail'),
]