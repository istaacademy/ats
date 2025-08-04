from .base import *
from .secure import *
from .packages import *
from decouple import config, Config
from datetime import timedelta

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

MINIO_STORAGE_ACCESS_KEY = config("MINIO_STORAGE_ACCESS_KEY")
MINIO_STORAGE_SECRET_KEY = config("MINIO_STORAGE_SECRET_KEY")
MINIO_STORAGE_ENDPOINT = config("MINIO_STORAGE_ENDPOINT")
MINIO_STORAGE_MEDIA_BUCKET_NAME = config("MINIO_STORAGE_MEDIA_BUCKET_NAME")


REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '5/day',
        'user': '30/day'
    }
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'ATS Ista Academy',
    'VERSION': '2.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=config("ACCESS_TOKEN_LIFETIME", cast=int)),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=config("REFRESH_TOKEN_LIFETIME", cast=int)),
    'AUTH_HEADER_TYPES': ('Bearer',),
}


