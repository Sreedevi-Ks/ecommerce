from django.contrib import admin
from .models import User
from .models import Product
from .models import Cart
from .models import Order
# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)