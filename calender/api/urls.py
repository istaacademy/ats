# urls.py
from django.urls import path
from .views import EventApiView

urlpatterns = [
    path('', EventApiView.as_view(), name='event'),
]
