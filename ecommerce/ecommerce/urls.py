"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from ecomapp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('ecomregister', ecomregister, name='ecomregister'),
    path('userindex/', userindex, name='userindex'),
    path('adminhome/', adminhome, name='adminhome'),
    path('products/', products, name='products'),
    path('orders/', orders, name='orders'),
    path('cart/', cart, name='cart'),
    path('profile/', profile, name='profile'),
    path('addproduct/', addproduct, name='addproduct'),
    path('saveproduct/', saveproduct, name='saveproduct'),
    path('adminproducts/', adminproducts, name='adminproducts'),
    path('logout/', logout, name='logout'),
    path('addtocart/<int:id>/', addtocart, name='addtocart'),
    path('deleteproduct/<int:id>/', deleteproduct, name='deleteproduct'),
    path('checkout/', checkout, name='checkout'),
    path('orders/', orders, name='orders'),
    path('paymentpage/', paymentpage, name='paymentpage'),
    path('increase_quantity/<int:id>/', increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:id>/', decrease_quantity, name='decrease_quantity'),
    path('remove_cart/<int:id>/', remove_cart, name='remove_cart'),
    path('adminorders/', adminorders, name='adminorders'),
]
