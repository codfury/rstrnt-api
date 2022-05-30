from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

class RegistrationSerializer(serializers.ModelSerializer):


    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(min_length=8, write_only=True,style={'input_type': 'password'},
        trim_whitespace=False)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'password')

    #validation of user
    def validate(self, args):
        username = args.get('username', None)
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('username already exists')})

        return super().validate(args)
  

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )
    


    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)

        attrs['user'] = user
        return attrs
        


