from rest_framework import serializers
from user.models import (
    User ,
    Profile,
)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password


class CreateUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name','password' , 'phone_number']
        extra_kwargs = {"password":{"write_only":True}}

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)



class SingInSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length = 11)

class VerificationCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        request = self.context.get("request")  # Get request object

        phone_number = data['phone_number']
        code = data['code']

        # Get session data
        session_code = request.session.get('verification_code')
        session_phone = request.session.get('phone_number')

        if not (session_phone and session_code):
            raise serializers.ValidationError("No verification code found. Please request a new code.")

        if session_phone == phone_number and str(session_code) == str(code):
            # Clear session after verification
            del request.session['verification_code']
            del request.session['phone_number']

            user, created = User.objects.get_or_create(phone_number=phone_number)

            refresh = RefreshToken.for_user(user)
            return {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }

        raise serializers.ValidationError("Invalid verification code.")

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'url_github', 'url_linkedin', "telephone", "national_code"]



