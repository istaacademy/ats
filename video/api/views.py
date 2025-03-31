from datetime import timedelta
from rest_framework import status
from utils.response_model import Result
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from video.models import Video
from video.utils import client
from decouple import config
import subprocess
import os

BUCKET_NAME = config("MINIO_STORAGE_MEDIA_BUCKET_NAME")



class VideoListView(APIView):
    serializer_class = None
    permission_classes = (IsAuthenticated, )
    def get(self, request, course_id, *args, **kwargs):
        try:
            videos = Video.objects.filter(course__id=course_id).order_by("order")
            if videos.exists():
                data = [
                    {
                        "title": video.title,
                        "time": video.time,  # Ensure this is a string/JSON-serializable value
                        "url": client.presigned_get_object(BUCKET_NAME, video.title, expires=timedelta(hours=1))
                    }
                    for video in videos
                ]
                return Result.data(data, message="get videos")
            return Result.error({"message": "No videos found"})
        except Exception as e:
            # Convert exception to string for JSON serialization
            return Result.error({"message": str(e)}, code=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UploadVideoView(APIView):
    """Handles video uploads to MinIO."""

    def post(self, request, *args, **kwargs):
        if 'file' not in request.FILES:
            return Result.error({"error": "No file provided"}, code=status.HTTP_400_BAD_REQUEST)

        file = request.FILES['file']
        file_name = file.name

        # Save video temporarily
        temp_file_path = f"/tmp/{file_name}"
        with open(temp_file_path, "wb+") as temp_file:
            for chunk in file.chunks():
                temp_file.write(chunk)

        # Upload to MinIO
        try:
            client.fput_object(BUCKET_NAME, file_name, temp_file_path)
        except Exception as e:
            return Result.error({"error": str(e)}, code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        finally:
            os.remove(temp_file_path)  # Ensure temp file is deleted

        return Result.data({"video_name": file_name}, message="File uploaded successfully",
                        code=status.HTTP_201_CREATED)

#
# class StreamVideoView(APIView):
#     # permission_classes = (IsAuthenticated, )
#     """Handles video uploads to MinIO."""
#     def post(self, request, video_id,  *args, **kwargs):
#         """Fetches video from MinIO and streams it to the RTMP server."""
#         # try:
#         print(video_id)
#         video_url = client.presigned_get_object(BUCKET_NAME, video_id, expires=timedelta(hours=1))
#         print(video_url)
#         # your_rtmp_server = config("RTMP_SERVER")
#         # rtmp_url = f"rtmp://{your_rtmp_server}/live/stream"
#         #
#         # # FFmpeg command to stream video to RTMP
#         # ffmpeg_cmd = [
#         #     "ffmpeg", "-re", "-i", video_url, "-c:v", "libx264", "-preset", "fast",
#         #     "-b:v", "1000k", "-maxrate", "1000k", "-bufsize", "2000k",
#         #     "-c:a", "aac", "-b:a", "128k", "-f", "flv", rtmp_url
#         # ]
#         #
#         # subprocess.Popen(ffmpeg_cmd)
#
#         return Result.data({"message": "Streaming started", "rtmp_url": rtmp_url})
#         #
#         # except Exception as e:
#         #     return Result.error({"error": str(e)}, code=500)