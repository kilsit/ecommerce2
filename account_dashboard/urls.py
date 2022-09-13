from django.urls import path
from .views import *


urlpatterns = [
    path("account/", account, name="account"),
    path('account_delete/<int:pk>/',  account_delete, name="account-delete"),
    # path('account_update/<int:pk>/',  account_update, name="account-update"),
    path('account_update/edit/<int:pk>', UpdatePostView.as_view(), name='account-update'),
]