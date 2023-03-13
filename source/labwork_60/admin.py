from django.contrib import admin

from labwork_60.models import Product, Order


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'category', 'amount', 'price')
    list_filter = ('title', 'category', 'amount', 'price')
    search_fields = ('title', 'category', 'price')
    fields = ('title', 'description', 'image', 'category', 'amount', 'price')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'phone_number', 'address', 'created_at')
    list_filter = ('products', 'username', 'phone_number', 'address', 'created_at')
    search_fields = ('products', 'username', 'phone_number', 'address')
    fields = ('pk', 'username', 'phone_number', 'address', 'created_at')
    ordering = ('-created_at',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
