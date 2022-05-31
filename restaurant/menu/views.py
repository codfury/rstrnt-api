from ast import keyword
import imp
from django.shortcuts import render
import rest_framework
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
from .models import Category, Item
from rest_framework import viewsets, mixins
from rest_framework import filters
from django.db.models import Q
from .serializers import ItemSerializer,CategorySerializer

class AdminAuthenticationPermission(permissions.BasePermission):
    ADMIN_ONLY_AUTH_CLASSES = [rest_framework.authentication.TokenAuthentication]

    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated:
            return user.is_superuser or \
                not any(isinstance(request._authenticator, x) for x in self.ADMIN_ONLY_AUTH_CLASSES) 
        return False


class ListMenuAPIView(generics.ListAPIView):
    search_fields = ['title','description',]
    filter_backends = (filters.SearchFilter,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        return self.queryset.filter(is_available=True)

# class SearchListMenuAPIView(generics.ListAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
    

#     def get_queryset(self):
#         print(self.request.query_params,self.request.data)
#         keyword=self.kwargs['keyword']
#         return self.queryset.filter(is_available=True).filter(Q(description__icontains=keyword) | Q(title__icontains=keyword))
    


class ItemDetailAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CategoryItems(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        return self.queryset.filter(category=self.kwargs['pk'])

class AddItemView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,AdminAuthenticationPermission)
    authentication_classes = (authentication.TokenAuthentication,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    def post(self, request):
        
        serializer = self.get_serializer(data = request.data)
        
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                    "Message": "Added Item",
                    }, status=status.HTTP_201_CREATED)
        else:
            
            return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class EditItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,AdminAuthenticationPermission)
    authentication_classes = (authentication.TokenAuthentication,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    
    

# Create your views here.
