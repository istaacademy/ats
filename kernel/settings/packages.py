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

INSTALLED_APPS.append("calender")
INSTALLED_APPS.append("volunteer")
INSTALLED_APPS.append("accounts")
INSTALLED_APPS.append("course")

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'ATS Ista Academy',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}
