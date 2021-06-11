from django.contrib import admin
# from django.contrib.auth.models import Group
from .models import Product, Cartitem
# Register your models here.
class ProductDesigns(admin.ModelAdmin):
      list_display = ("name", "price")



class CartitemDesigns(admin.ModelAdmin):
      list_display = ("name", "id")


admin.site.register(Product, ProductDesigns)
admin.site.register(Cartitem, CartitemDesigns)

# admin title
admin.site.site_header= "Shoes Place"
