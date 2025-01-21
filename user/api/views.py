from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from api.serializers import CreateUserSerilaizers
from user.models import User


class UserCreateAPIView(APIView):
  def post(Self , request , *args, **kwargs):
    serilizer = CreateUserSerilaizers(data = request.data)
    
    if serilizer.is_valid():
        user = serilizer.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response (
           {
              'message' : 'User created successfully' , 
              'access' : access_token , 
              'refresh' : str(refresh)
           } , status=status.HTTP_201_CREATED
        )
    
    return Response (serilizer.errors , status=status.HTTP_400_BAD_REQUEST)