# urls.py
from django.urls import path
from .views import VolunteerApiview

urlpatterns = [
    path('', VolunteerApiview.as_view(), name='volunteer'),
]
