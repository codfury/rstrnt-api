from unicodedata import name
from django.db import models
from menu.models import Item
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 


class CartItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date_updated = models.DateField(auto_now_add=True)

    def sub_total(self):
        return self.item.price * self.quantity

    def __str__(self) -> str:
        return self.item
    
# Create your models here.
