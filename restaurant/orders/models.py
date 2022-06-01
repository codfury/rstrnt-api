from ast import mod
from django.db import models
from unicodedata import name
from django.db import models
from menu.models import Item
from django.contrib.auth.models import User


class Order(models.Model):
    STATUS = (
        ('Processing', 'Processing'),
        ('Cooking', 'Cooking'),
        ('Serving', 'Serving'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=500)
    order_total = models.FloatField()
    is_ordered = models.BooleanField(default=False)
    status=models.CharField(max_length=20, choices=STATUS, default='Processing')
    date_added = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    total =models.PositiveIntegerField()


    def __str__(self):
        return self.item.title


# Create your models here.
