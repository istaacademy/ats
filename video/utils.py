from minio import Minio
from django.conf import settings

client = Minio(
    settings.MINIO_STORAGE_ENDPOINT.replace("http://", "").replace("https://", ""),
    access_key=settings.MINIO_STORAGE_ACCESS_KEY,
    secret_key=settings.MINIO_STORAGE_SECRET_KEY,
    secure=False  # Set to True if using HTTPS
)

def upload_video(file, filename, bucket_name = settings.MINIO_STORAGE_MEDIA_BUCKET_NAME):
    client.put_object(bucket_name, filename, file, length=-1, part_size=10*1024*1024)
    return f"{settings.MINIO_STORAGE_ENDPOINT}/{bucket_name}/{filename}"