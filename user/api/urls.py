from django.urls import path
from user.api.views import *

urlpatterns = [
    path('sign-up', SignUpAPIView.as_view(), name='sign-up'),
    path('sign-in', SingInView.as_view(), name='sign-in'),
    path('verfication-code', VerificationCodeView.as_view(), name='verification'),
    path('profile/<int:user_id>', ProfileAPIView.as_view(), name='user-profile'),
    path('profile/update/<int:user_id>', UpdateProfileAPIView.as_view(), name='update-profile'),
]
