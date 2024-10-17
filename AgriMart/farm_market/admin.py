from django.contrib import admin

# Register your models here.
from .models import Farmer, Product, Cart, CartItem, Order, DeliveryCrew

admin.site.register(Farmer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(DeliveryCrew)