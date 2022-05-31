from django.urls import path
from .views import ListMenuAPIView,ItemDetailAPIView,CategoryItems,AddItemView,EditItemView
app_name = 'menu'

urlpatterns = [
path('items/', ListMenuAPIView.as_view(), name= 'menu_items'),
# path('search/<str:keyword>', SearchListMenuAPIView.as_view(), name= 'search_menu'),
path('items/<int:pk>/', ItemDetailAPIView.as_view({'get': 'retrieve'}), name= 'single_item'),
path('categories/<int:pk>/', CategoryItems.as_view({'get': 'list'}), name='category_items'),
path('add/', AddItemView.as_view(), name= 'add_item'),
path('edit/<int:pk>/', EditItemView.as_view(), name='edit_item'),



]