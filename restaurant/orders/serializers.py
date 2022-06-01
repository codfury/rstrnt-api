
from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
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
from .models import Order,OrderItem
from cart.models import CartItem
from menu.models import Item
from django.shortcuts import get_object_or_404
import urllib.request

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('__all__'
    
        )
        read_only_fields = ('user', 'date_added','is_ordered','order_total','status')
        model = Order


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        read_only_fields=('order','item','total','quantity')
        model = OrderItem