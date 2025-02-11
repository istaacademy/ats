from .base import INSTALLED_APPS

# ###########
# Third-party apps #
#############

INSTALLED_APPS.append("rest_framework")
INSTALLED_APPS.append('drf_spectacular')
INSTALLED_APPS.append('apptemplates')
INSTALLED_APPS.append('django_prometheus')
INSTALLED_APPS.append('corsheaders')

# ##########
# local apps
# ##########

# 'jalali_date',
INSTALLED_APPS.append("user")
INSTALLED_APPS.append("course")
INSTALLED_APPS.append("video")
INSTALLED_APPS.append("comment")

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'ATS Ista Academy',
    'VERSION': '2.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}


