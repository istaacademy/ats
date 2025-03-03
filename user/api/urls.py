from django.urls import path
from api.views import CreateUserSerilaizers ,SingInView , UpdateProfileAPIView , ProfileAPIView ,GenerateTokenAPIView ,RefreshTokenAPIView ,ValidateTokenAPIView

urlpatterns = [
    path('register/', CreateUserSerilaizers.as_view(), name='register'),
    path('signin/', SingInView.as_view(), name='signin'),
    path('profile/<int:user_id>/', ProfileAPIView.as_view(), name='user-profile'),
    path('profile/update/<int:user_id>/', UpdateProfileAPIView.as_view(), name='update-profile'),
    path('api/generate-token/', GenerateTokenAPIView.as_view(), name='generate_token'),
    path('api/refresh-token/', RefreshTokenAPIView.as_view(), name='refresh_token'),
    path('api/validate-token/', ValidateTokenAPIView.as_view(), name='validate_token'),
]
