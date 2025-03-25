from rest_framework import serializers
from user.models import (
    User ,
    Profile,
)
from django.contrib.auth.hashers import make_password


class CreateUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name','password' , 'phone']

        read_only_fields = [] 
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.password = make_password(password) 
        user.save()
        return user


class SingInSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length = 11)


class VerificationSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11)
    code = serializers.CharField(max_length = 5)


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'url_github', 'url_linkedin', "telephone", "national_code"]



