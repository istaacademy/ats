from .base import *
from .secure import *
from .packages import *
from decouple import config

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(',')])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"


# MinIO settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = config("ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = config("SECRET_KEY")
AWS_STORAGE_BUCKET_NAME = config("BUCKET_NAME")
AWS_S3_ENDPOINT_URL = config("MINIO_URL")
AWS_S3_REGION_NAME = 'us-east-1'  # or your MinIO region
AWS_S3_CUSTOM_DOMAIN = f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}'
AWS_S3_FILE_OVERWRITE = False  # To prevent overwriting files with the same name
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_AUTH = True

REDIS_HOST = config("REDIS_HOST")
REDIS_PORT = config("REDIS_PORT", cast=int)
VERSION = "V1"

SECRET_KEY = config('SECRET_KEY')
