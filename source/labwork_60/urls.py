from django.urls import path

from labwork_60.views.base import IndexView, IndexRedirectView
from labwork_60.views.products import ProductDetailView, ProductCreateView, ProductDeleteView, ProductUpdateView

from labwork_60.views.cart import add_to_cart, CartView, CartProductDeleteView

from labwork_60.views.order import OrderCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products', IndexView.as_view(), name='index'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product/add', ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/confirm_delete', ProductDeleteView.as_view(), name='confirm_delete'),
    path('product/<int:pk>/edit', ProductUpdateView.as_view(), name='product_edit'),
    path('add-to-cart/<int:pk>/', add_to_cart, name='add_product_to_cart'),
    path('cart', CartView.as_view(), name='cart'),
    path('cart/<int:pk>/delete', CartProductDeleteView.as_view(), name='delete_product_from_cart'),
    path('cart/create_order', OrderCreateView.as_view(), name='create_order')
]
