from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from api.serializers import CreateUserSerilaizers , SinginSerializer, VerificationSerializer , ProfileSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from user.models import User , Profile


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


class SingInView(APIView):
   
   def post(self , request):
      serilizer = SinginSerializer(data = request.data)
      if serilizer.is_valid():
          return Response({"message" : "verification code sent"} , status=status.HTTP_200_OK)
      
      return Response(serilizer.errors , status=status.HTTP_400_BAD_REQUEST)
   


class VerificationView(APIView):
   def post(self , request):
      serializer = VerificationSerializer(request = request.data)

      if serializer.is_valid():
         return Response({
            "refresh" : serializer.validated_data['refresh'],
            "access" : serializer.validated_data['access'],

         }, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

class ProfileAPIView(APIView):
   authentication_classes = [JWTAuthentication]
   permission_classes = [IsAuthenticated]


   def get (self , request):
      profile = Profile.objects.get(user = request.user)
      serializer = ProfileSerializer(profile)

      return Response(serializer.data)
   

   