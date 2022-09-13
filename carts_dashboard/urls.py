from django.urls import path
from .views import *
urlpatterns = [
    path("cart_dashboard/", cart_dashboard, name="cart_dashboard"),
    path('cart_delete/<int:pk>/',  cart_delete, name="cart-delete"),
]