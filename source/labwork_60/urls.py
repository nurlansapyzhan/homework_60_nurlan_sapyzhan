from django.urls import path

from labwork_60.views.base import products_view
from labwork_60.views.products import product_view, add_product_view, delete_product, confirm_delete, edit_product

urlpatterns = [
    path('', products_view, name='index'),
    path('products', products_view, name='index'),
    path('products/<int:pk>', product_view, name='product_detail'),
    path('product/add', add_product_view, name='add_product'),
    path('product/<int:pk>/delete', delete_product, name='product_delete'),
    path('product/<int:pk>/confirm_delete', confirm_delete, name='confirm_delete'),
    path('product/<int:pk>/edit', edit_product, name='product_edit'),
]
