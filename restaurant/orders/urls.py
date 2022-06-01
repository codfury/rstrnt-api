from django.urls import path
from .views import CreateOrderView,OrderView,OrderDetailView,OrderCancelView

urlpatterns = [
    path('create/', CreateOrderView.as_view(), name='buy'),
    path('past_orders/', OrderView.as_view({'get': 'list'}), name='allorders'),
    path('past_orders/<int:pk>/', OrderDetailView.as_view({'get': 'list'}), name='singleorder'),
    path('cancel/<int:pk>/', OrderCancelView.as_view(), name='cancelorder'),


]