from django.urls import path
from .views import *

urlpatterns = [
    path('add_category/', add_category, name="add_category"),
    path('category/', category, name="category"),
    path('<int:pk>/', category_delete, name="category-delete"),
    path('category_update/<int:pk>/', category_update, name="category-update"),
    # path('category/<int:pk>/', category, name="category-delete"),
  
]

