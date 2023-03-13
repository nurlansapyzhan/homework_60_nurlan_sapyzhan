from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView

from labwork_60.models import ProductInCart, Product


def add_to_cart(request, pk):
    product = Product.objects.get(pk=pk)
    if product.amount <= 0:
        return redirect('index')
    try:
        cart_item = ProductInCart.objects.get(product=product)
        if cart_item.amount < product.amount:
            cart_item.amount += 1
            cart_item.save()
    except ProductInCart.DoesNotExist:
        ProductInCart.objects.create(product=product)
        cart_item = ProductInCart.objects.get(product=product)
        if cart_item.amount < product.amount:
            cart_item.amount += 1
            cart_item.save()
    return redirect('index')


class CartView(ListView):
    model = ProductInCart
    template_name = 'cart.html'
    context_object_name = 'cart_items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        total = sum(item.product.price * item.amount for item in context['cart_items'])
        context['total'] = total
        return context


class CartProductDeleteView(DeleteView):
    model = ProductInCart
    template_name = 'cart.html'
    success_url = reverse_lazy('cart')
