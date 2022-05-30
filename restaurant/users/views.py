from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework import generics, authentication, permissions
from .serializers import RegistrationSerializer, LoginSerializer

class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "Message": "User created successfully",
                
                "User": serializer.data}, status=status.HTTP_201_CREATED
                )
        
        return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(ObtainAuthToken):

    serializer_class = LoginSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class LogoutAPIView(generics.GenericAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        # simply delete the token
        request.user.auth_token.delete()
        return Response({"message":"Logged Out and succefully Deleted Token"}, status=status.HTTP_200_OK)
   
class ProfileView(generics.GenericAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
                 

    def get(self, request):
        content = {'user':str(request.user)}
        return Response(content)




# Create your views here.
