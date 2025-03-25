from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from video.models import Video


class VideoListView(APIView):
    serializer_class = None
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
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
                return Response(data, status=status.HTTP_200_OK)
            return Response({"message": "No videos found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Convert exception to string for JSON serialization
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)