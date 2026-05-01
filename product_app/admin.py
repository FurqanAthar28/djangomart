from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'short_description', 'long_description', 'img_link', 'category', 'upload_date', 'product_slug')
    search_fields = ('title', 'category')
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity')
    list_filter = ('id','user')
    
@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'created_at', 'first_name', 'last_name', 'email', 'mobile', 'address_line1', 'address_line2', 'country', 'city', 'state', 'zip_code')
    list_filter = ('id','user', 'email', 'mobile')