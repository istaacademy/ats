from django.urls import path
from user.api.views import *

urlpatterns = [
    path('sign-up/', SignUpAPIView.as_view(), name='sign-up'),
    path('sign-in/', SingInView.as_view(), name='sign-in'),
    path('verfication-code', VerificationView.as_view(), name='verification'),
    path('profile/<int:user_id>', ProfileAPIView.as_view(), name='user-profile'),
    path('profile/update/<int:user_id>', UpdateProfileAPIView.as_view(), name='update-profile'),
    path('refresh-token/', RefreshTokenAPIView.as_view(), name='refresh_token'),
    path('validate-token/', ValidateTokenAPIView.as_view(), name='validate_token'),
]
