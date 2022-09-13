from django.urls import path
from .views import *
urlpatterns = [
    path("order_dashboard/", order_dashboard, name="order_dashboard"),
    path("order_product/", order_product, name="order_product"),
    path('order_dashboard_delete/delete/<int:pk>/', order_dashboard_delete, name="order-delete"),
]