from itertools import product
from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework import generics, authentication, permissions


from rest_framework import viewsets, mixins
from django.shortcuts import get_object_or_404

from menu.models import Item
from .serializers import OrderSerializer,OrderItemSerializer
from .models import Order,OrderItem
from cart.models import CartItem


class CreateOrderView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)
    queryset = CartItem.objects.all()
    serializer_class = OrderSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        
        if(serializer.is_valid()):
            
            total=0
            
            for item in CartItem.objects.filter(user=self.request.user):
                        total+=(item.sub_total())
                        
            order = serializer.save(user=self.request.user,is_ordered='True',order_total=total)
            for item in CartItem.objects.filter(user=self.request.user):
                        op = OrderItem(order=order,item = item.item, quantity=item.quantity,total=item.sub_total())
                        op.save()
                        item.delete()
            return Response({
                    "Message": "Ordered",
                    
                    "Details": serializer.data,
                    "Total":total,
                    }, status=status.HTTP_201_CREATED)
        else:
            return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            
    
    def get_queryset(self):
        queryset =self.queryset
        return queryset.filter(
            user=self.request.user
        )

class OrderView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)   
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


    def get_queryset(self):
        queryset =self.queryset
        return queryset.filter(
            user=self.request.user,
            is_ordered =True
        )


class OrderDetailView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)   
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        queryset =self.queryset
        order_id=self.kwargs.get('pk', None)
        items=queryset.filter(
            order = order_id
        )
        if(items.exists() and get_object_or_404(Order,id = order_id).is_ordered):

        
            return queryset.filter(
            order = order_id,
        )

        return None



class OrderCancelView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self,request,pk):
        order_id=pk
        print(self.request.user)
        queryset =get_object_or_404(Order,id = order_id,user=self.request.user)
        
        if(queryset and queryset.is_ordered):
            
            if(queryset.status!="Processing"):
                return Response({"Errors": "Can't cancel order is already proccessed kindly talk to the manager"}, status=status.HTTP_400_BAD_REQUEST)

            queryset.is_ordered=False
            queryset.status='Cancelled'
            queryset.save()
            return Response({
                    "Message": f"Order {order_id} Cancelled",
                    }, status=status.HTTP_201_CREATED)
        else:
            return Response({"Errors": "Order Not Found or cancelled"}, status=status.HTTP_400_BAD_REQUEST)




    


# Create your views here.
