from rest_framework import status
from utils.response_model import Result
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from video.models import Video


class VideoListView(APIView):
    serializer_class = None
    permission_classes = [IsAuthenticated]
    def get(self, request, course_id, *args, **kwargs):
        try:
            videos = Video.objects.filter(course__id=course_id)
            if videos.exists():  # Better than checking "if videos"
                data = [
                    {
                        "title": video.title,
                        "time": video.time,  # Ensure this is a string/JSON-serializable value
                        "url": video.file_url
                    }
                    for video in videos
                ]
                return Result.data(data, message="get videos")
            return Result.error({"message": "No videos found"})
        except Exception as e:
            # Convert exception to string for JSON serialization
            return Result.error({"message": str(e)}, code=status.HTTP_500_INTERNAL_SERVER_ERROR)