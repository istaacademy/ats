from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from api.serializers import CreateUserSerilaizers , SinginSerializer, VerificationSerializer , ProfileSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from user.models import Profile
from user.utils import refresh_token ,generate_token , validate_token

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


   def get(self, request, user_id):
        try:
            profile = Profile.objects.get(user__id=user_id)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({"message": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
        
class UpdateProfileAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self , request , user_id):
      try:
         profile = Profile.objects.get(user_id=user_id)
         serializer = ProfileSerializer(profile , data = request.data , partial = True)
         if serializer.is_valid():
            serializer.save()
            return Response (serializer.data , status=status.HTTP_200_OK)
         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
      except Profile.DoesNotExist:
         return Response ({"meesage" : "User Not Found."} , status=status.HTTP_404_NOT_FOUND)
      
class GenerateTokenAPIView(APIView):
   def post(self , request):
      username = request.data.get('username')
      if not username:
         return Response ({'error' :"username is required"} , status=status.HTTP_400_BAD_REQUEST)

      token =generate_token(username)
      return Response({"token" : token } , status=status.HTTP_200_OK)
   
class RefreshTokenAPIView(APIView):
    def post(self, request):
        old_token = request.data.get('token')
        if not old_token:
            return Response({"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        new_token = refresh_token(old_token)
        return Response({"new_token": new_token}, status=status.HTTP_200_OK)


class ValidateTokenAPIView(APIView):
    def post(self, request):
        token = request.data.get('token')
        if not token:
            return Response({"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        username = validate_token(token)
        if username:
            return Response({"username": username}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)