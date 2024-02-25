from .base import INSTALLED_APPS

# ###########
# Third-party apps #
#############

INSTALLED_APPS.append("rest_framework")
INSTALLED_APPS.append('drf_spectacular')
INSTALLED_APPS.append('apptemplates')

# ##########
# local apps
# ##########

INSTALLED_APPS.append("calender")
INSTALLED_APPS.append("volunteer")

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'ATS Ista Academy',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}
