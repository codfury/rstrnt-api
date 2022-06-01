from django.urls import path
from .views import AddCartItem

urlpatterns = [
    path('mycart', AddCartItem.as_view(), name='mycart'),



]