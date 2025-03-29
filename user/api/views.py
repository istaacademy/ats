from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import random
from user.api.serializers import (
    CreateUserSerializers ,
    SingInSerializer,
    VerificationCodeSerializer ,
    ProfileSerializer
)
from user.models import User
from rest_framework.permissions import IsAuthenticated
from user.models import Profile

class SignUpAPIView(APIView):
    serializer_class = CreateUserSerializers

    def post(Self , request , *args, **kwargs):
        serializer = CreateUserSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (
               {
                  'message' : 'User created successfully' ,
                   "data": serializer.data
               } , status=status.HTTP_201_CREATED
            )
        return Response (serializer.errors , status=status.HTTP_400_BAD_REQUEST)


class SingInView(APIView):
   serializer_class = SingInSerializer

   def post(self , request):
      serializer = SingInSerializer(data = request.data)
      if serializer.is_valid():
        phone_number = serializer.validated_data['phone_number']
        user =  User.objects.filter(phone_number=phone_number)
        if not user.exists():
           return Response({"message": "کاربری با این شماره تلفن وجود ندارد."}, status=status.HTTP_404_NOT_FOUND)

        verification_code = random.randint(10000, 100000)
        # Save to session
        request.session['verification_code'] = verification_code
        request.session['phone_number'] = phone_number
        request.session.set_expiry(300)  # 5 minutes expiry
        # Send the code via SMS here

        return Response({"message": "کد تأیید ارسال شد."})

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerificationCodeView(APIView):
    serializer_class = VerificationCodeSerializer

    def post(self , request, *args, **kwargs):
        serializer = VerificationCodeSerializer(data = request.data, context={'request': request})
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response({"message":serializer.errors, "code": 400}, status=status.HTTP_400_BAD_REQUEST)

class ProfileAPIView(APIView):
   permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
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