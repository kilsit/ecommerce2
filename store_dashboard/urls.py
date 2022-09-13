
from django.urls import path
from .views import *
urlpatterns = [
    path("", admin_dashboard, name="admin_dashboard"),
    path("store_dashboard/", store_dashboard, name="store_dashboard"),
    path('store_dashboard/delete/<slug:product_slug>/',  store_dashboard_delete, name="store-delete"),
    path('store_dashboard/update/<slug:product_slug>/',  store_dashboard_update, name="store-update"),
    path("store_form/", store_form, name="store_form"),
    path("variation/", variation, name="variation"),
    path('variation_delete/<int:pk>/', variation_delete, name="variation-delete"),
    path('variation_update/<int:pk>/', variation_update, name="variation-update"),
    path("productgallery/", productgallery, name="productgallery"),
]