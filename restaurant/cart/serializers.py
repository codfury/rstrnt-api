from itertools import product
from rest_framework import serializers
from .models import CartItem
from .models import Item

class CartItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CartItem
        fields = ('__all__')
        read_only_fields = ('user', 'date_updated')
    
