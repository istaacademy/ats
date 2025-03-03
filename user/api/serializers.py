from rest_framework import serializers
from user.models import User , Profile 
from django.contrib.auth.hashers import make_password
import random
from rest_framework_simplejwt.tokens import RefreshToken


class CreateUserSerilaizers(serializers.Serializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','first_name', 'last_name','password' , 'phone']

        read_only_fields = [] 
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.password = make_password(password) 
        user.save()
        return user
    
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = User.objects.filter(username=username).first()
        if not user or user.password != password:
            raise serializers.ValidationError("نام کاربری یا رمز عبور اشتباه است")

        if not user.is_active:
            raise serializers.ValidationError("کاربر غیرفعال است")

        attrs["user"] = user
        return attrs




class SinginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length = 11)

    def validate(self ,attrs):
        phone = attrs.get('phone')
        user, created  = User.objects.get_or_create(phone=phone)
        if not user :
            raise serializers.ValidationError("کاربری با این شماره تلفن وجود ندارد.")
        

        verification_code  = random.randit(1000 , 99999)
        user.verification_code = verification_code
        user.save()  #change to session django


        print(f"verifaction Code : {verification_code}")

        return attrs
    


class VerificationSerializer(serializers.Serializer):
    verification_code = serializers.CharField(max_length = 5)

    def validate(self, attrs):
        phone = attrs.get('phone')
        verification_code = attrs.get('verification_code')


        user = User.objects.filter(phone=phone).first()
        if not user:
            raise serializers.ValidationError("کاربری با این شماره تلفن وجود ندارد.")
        if user.verification_code != verification_code:
            raise serializers.ValidationError("کد تأیید نامعتبر است.")


        return attrs



class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = Profile
        fields = ['name', 'url_github', 'url_linkdin', 'telephone',
                   'address', 'national_code', 'role']
        


