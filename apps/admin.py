from django.contrib import admin

# from django.contrib.auth.models import Group
from .models import *

# Register your models here.


class CartitemDesigns(admin.ModelAdmin):
    list_display = ("cart", "id")


admin.site.register(Products)
admin.site.register(CartProduct, CartitemDesigns)

# admin title
admin.site.site_header = "Shoes Place"

admin.site.register([Category, Cart, Order, Customer])
