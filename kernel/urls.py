from django.contrib import admin
from django.urls import (
    path,
    include,
)

from django.conf.urls.static import static
from django.conf import settings


from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
                  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                  # Optional UI:
                  path('ista/', admin.site.urls),
                  path('api/volunteer', include('volunteer.api.urls')),
                  path('api/calender', include('calender.api.urls')),
                  # Optional UI:
                  # Optional UI:
                  path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                  path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

              ] + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
