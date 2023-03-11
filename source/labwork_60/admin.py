from django.contrib import admin

from labwork_60.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'category', 'amount', 'price')
    list_filter = ('title', 'category', 'amount', 'price')
    search_fields = ('title', 'category', 'price')
    fields = ('title', 'description', 'image', 'category', 'amount', 'price')


admin.site.register(Product, ProductAdmin)
