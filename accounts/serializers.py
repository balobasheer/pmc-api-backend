from django.contrib.auth.models import User
from rest_framework import serializers

from rest_framework_simplejwt.serializers import  TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login

from .models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
      
    class Meta:
        model = User
        fields = [
                    'id',
                    'username', 
                    'first_name', 
                    'last_name', 
                    'email', 
                    'phone_number', 
                    'post_code',
                    'role',
                    'is_active',
                    'created', 
                    'updated'
                    ]
        read_only_field = ['is_active']


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    password = serializers.CharField(
        write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(required=False)
    id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    class Meta:
        model = User
        fields = [
                    'id',
                    'first_name', 
                    'last_name',
                    'username',
                    'email', 
                    'phone_number',
                    'role', 
                    'post_code',
                    'password', 
                    'password2',
                    'is_subscribed',
                    ]
        read_only_field = ['is_deleted', 'username', 'id']

    def validate(self, attrs):
        
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        if not attrs['role']:
            raise serializers.ValidationError(
                {"role": "Kindly, select a role."})
        
        return attrs

    def create(self, validated_data):
        
        username = None
        if validated_data['first_name'] and validated_data['last_name']:
            username = f"{validated_data['first_name']} {validated_data['last_name']}"
        else:
            username = validated_data['email'].split('@')[0]

        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=username,
            phone_number=validated_data['phone_number'],
            post_code=validated_data['post_code'],
            is_subscribed=validated_data['is_subscribed'],
            role=validated_data['role'],
           
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        if api_settings.UPDATE_LAST_LOGIN and data['user'].is_deleted != False:
            update_last_login(None, self.user)
        else:
            return f"Hi, You are no more an active {self.user.role}"
        return data