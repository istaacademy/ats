import boto3
from django.conf import settings


class Bucket:
    """
     CDN Bucket Manager
     init method creates connection.
     Note:
         none of these methods are async. use public interface in tasks.py modules instead.
    """
    def __init__(self):
        session = boto3.session.Session()
        # # Initialize MinIO client
        self.conn = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
            region_name=settings.AWS_S3_REGION_NAME
        )

    def upload_to_minio(self, video_file):
        """
        Uploads the video to MinIO and returns the URL to access it.
        """


        # Upload the file to MinIO
        bucket_name = settings.AWS_STORAGE_BUCKET_NAME
        file_key = f"videos/{video_file.name}"

        try:
            # Upload the file
            self.conn.upload_fileobj(video_file, bucket_name, file_key)

            # Generate a URL for accessing the video
            video_url = f"{settings.AWS_S3_CUSTOM_DOMAIN}/{file_key}"

            return video_url
        except Exception as e:
            print(f"Error uploading video to MinIO: {e}")
            return None

    def delete_object(self, key):
        self.conn.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=key)
        return True

bucket = Bucket()