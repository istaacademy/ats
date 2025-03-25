from celery import shared_task
from services.minio.bucket import bucket


@shared_task(queue='video', default_retry_delay=5, retry_kwargs={'max_retries': 5})
def upload_video(_id=1):
    from video.models import Video
    video = Video.objects.filter(id=_id).first()
    if video.video_file:
        return f"Video {video.title} uploaded successfully"
    else:
        return "No video file found."
