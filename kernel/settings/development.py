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

REDIS_HOST = config("REDIS_HOST")
REDIS_PORT = config("REDIS_PORT", cast=int)
VERSION = "V1"

SECRET_KEY = config('SECRET_KEY')


SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 1209600
SESSION_COOKIE_NAME = 'my_session_cookie'
SESSION_COOKIE_SECURE = True
SESSION_SAVE_EVERY_REQUEST = True


MINIO_STORAGE_ACCESS_KEY = config("MINIO_STORAGE_ACCESS_KEY")
MINIO_STORAGE_SECRET_KEY = config("MINIO_STORAGE_SECRET_KEY")
MINIO_STORAGE_ENDPOINT = config("MINIO_STORAGE_ENDPOINT")
MINIO_STORAGE_MEDIA_BUCKET_NAME = config("MINIO_STORAGE_MEDIA_BUCKET_NAME")