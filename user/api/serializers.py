from rest_framework import serializers
from user.models import User , Profile 
from django.contrib.auth.hashers import make_password




class CreateUserSerilaizers(serializers.Serializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','first_name', 'last_name','password']

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


