from django.urls import path
from video.api.views import *

urlpatterns = [
    path('videos/<int:course_id>', VideoListView.as_view(), name='video-list'),
    path('video/upload', UploadVideoView.as_view(), name='video-stream'),
]
