from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
import random
from user.api.serializers import (
    CreateUserSerializers ,
    SingInSerializer,
    VerificationSerializer ,
    ProfileSerializer
)
from user.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from user.models import Profile
from user.utils import refresh_token ,generate_token , validate_token

class SignUpAPIView(APIView):
    serializer_class = CreateUserSerializers

    def post(Self , request , *args, **kwargs):
        serializer = CreateUserSerializers(data = request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response (
               {
                  'message' : 'User created successfully' ,
                   "data": user
               } , status=status.HTTP_201_CREATED
            )
    
        return Response (serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class RefreshTokenAPIView(APIView):
    serializer_class = None
    def post(self, request, *args, **kwargs):
        old_token = request.data.get('token')
        if not old_token:
            return Response({"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        new_token = refresh_token(old_token)
        return Response({"new_token": new_token}, status=status.HTTP_200_OK)


class ValidateTokenAPIView(APIView):
    serializer_class = None
    def post(self, request):
        token = request.data.get('token')
        if not token:
            return Response({"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        username = validate_token(token)
        if username:
            return Response({"username": username}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)




class SingInView(APIView):
   serializer_class = SingInSerializer

   def post(self , request):
      serializer = SingInSerializer(data = request.data)
      if serializer.is_valid():
        phone = serializer.validated_data['phone']
        user =  User.objects.get(phone=phone)
        if not user:
           return Response({"message": "کاربری با این شماره تلفن وجود ندارد."}, status=status.HTTP_404_NOT_FOUND)

        verification_code = random.randint(1000, 99999)
        # Save to session
        request.session['verification_code'] = verification_code
        request.session['phone'] = phone
        request.session.set_expiry(300)  # 5 minutes expiry
        # Send the code via SMS here

        return Response({"message": "کد تأیید ارسال شد."})

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerificationView(APIView):
    serializer_class = VerificationSerializer

    def post(self , request):
          serializer = VerificationSerializer(request = request.data)
          if serializer.is_valid():
              submitted_phone = request.data.get('phone')
              submitted_code = request.data.get('code')

              # Get from session
              session_code = request.session.get('verification_code')
              session_phone = request.session.get('phone')

              if (session_phone == submitted_phone
                      and str(session_code) == str(submitted_code)):
                  # Clear session after verification
                  del request.session['verification_code']
                  del request.session['phone']

                  return Response({
                          "refresh": serializer.validated_data['refresh'],
                          "access": serializer.validated_data['access'],
                          "message": "احراز هویت موفقیت آمیز بود."

                      }, status=status.HTTP_200_OK)
              return Response({"message": "کد تأیید نامعتبر است."}, status=status.HTTP_400_BAD_REQUEST)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProfileAPIView(APIView):
   # authentication_classes = [JWTAuthentication]
   # permission_classes = [IsAuthenticated]
   serializer_class = None

   def get_object(self, pk):
       try:
           return Profile.objects.get(pk=pk)
       except Profile.DoesNotExist:
           return None

   def get(self, request, user_id):
       profile = self.get_object(user_id)
       if not profile:
           return Response(data={"message": "Not found", "data": {}}, status=status.HTTP_404_NOT_FOUND)
       serializer = ProfileSerializer(profile)
       return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateProfileAPIView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

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