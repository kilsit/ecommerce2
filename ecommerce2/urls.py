"""ecommerce2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from gettext import install
from socket import timeout
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls)s,
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('securelogin/', admin.site.urls),
    path('', include("ecommapp.urls")),
    path('store/', include("store.urls")),
    path('carts/', include("carts.urls")),
    path('accounts/', include("accounts.urls")),
    path('orders/', include("orders.urls")),
    path('store_dashboard/', include("store_dashboard.urls")),
    path('account_dashboard/', include("account_dashboard.urls")),  
    path('order_dashboard/', include("order_dashboard.urls")),
    path('carts_dashboard/', include("carts_dashboard.urls")), 
    path('category_dashboard/', include("category_dashboard.urls")),
    path('contact/', include("contact.urls")),
    # path('category/', include("category.urls")),   
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# i have to install django-session-timeout using pip  install django-session-timeout