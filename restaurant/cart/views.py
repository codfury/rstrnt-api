import imp
from itertools import product
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
from .serializers import CartItemSerializer
from .models import CartItem
from rest_framework import viewsets, mixins
from .models import CartItem
from menu.models import Item
from django.shortcuts import get_object_or_404
from .serializers import CartItemSerializer


class AddCartItem(generics.ListCreateAPIView):    
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer



    def post(self, request):
        
        serializer = self.get_serializer(data = request.data)
        quantity= int(request.data['quantity'])
        item_id= int(request.data['item'])
        
        if(serializer.is_valid()):
            

            if(CartItem.objects.filter(user=self.request.user,item=item_id).exists()):
                curr=CartItem.objects.get(user=self.request.user,item=item_id)
                
                if(quantity==0):
                    
                    curr.delete()
                    total=0
                    for item in CartItem.objects.filter(user=self.request.user):
                        total+=(item.sub_total())
                    return Response({
                    "Message": "Item deleted",
                    
                    "Item": Item.objects.get(id=item_id).title,
                    "Total Cart Value":total}, status=status.HTTP_201_CREATED
                    )
                    
                else:
                    
                    curr.quantity=request.data['quantity']
                    curr.save()
                    total=0
                    for item in CartItem.objects.filter(user=self.request.user):
                        total+=int(item.sub_total())
                    return Response({
                    "Message": "Item Succefully updated to cart",
                    
                    "Item": Item.objects.get(id=item_id).title,
                    "Total Cart Value":total}, status=status.HTTP_201_CREATED
                    )


            else:
                if(quantity==0):
                    return Response({"Errors": 'quantity cant be 0 for the new item to be added to cart'}, status=status.HTTP_400_BAD_REQUEST)

                
                serializer.save(user=self.request.user)
                total=0
                for item in CartItem.objects.filter(user=self.request.user):
                        total+=item.sub_total()
                return Response({
                    "Message": "Item Succefully added to cart",
                    
                    "Details": serializer.data,
                    "Total Cart Value":total}, status=status.HTTP_201_CREATED
                    )
            
        
        return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def get_queryset(self):
        print(self.request.data)
        queryset =self.queryset
        return queryset.filter(
            user=self.request.user
        ).order_by('-date_updated')

        
# Create your views here.
