from django.urls import path
from api.views import CreateUserSerilaizers ,SingInView , VerificationView , ProfileAPIView

urlpatterns = [
    path('register/', CreateUserSerilaizers.as_view(), name='register'),
    path('signin/', SingInView.as_view(), name='signin'),
    path('verify/', VerificationView.as_view(), name='verify'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
]
