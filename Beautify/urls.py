"""Beautify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include

# import pdb;pdb.set_trace()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('acc/',include('account.urls')),
    path('cart/',include('cart.urls')),
    path('payment/',include('payment.urls')),
    path('products/',include('products.urls')),
    path('orders/',include('orders.urls')),
    path('folders/',include('folders.urls')),
    
    # Keep this at last (as this compares in sequence from top to bottom)
    path('',include('main.urls')),
    
    
]
