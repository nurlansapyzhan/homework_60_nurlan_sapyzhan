from django.shortcuts import redirect
from django.views.generic import CreateView

from labwork_60.models import Order, ProductInCart, OrderProducts

from labwork_60.forms import OrderForm


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'create_order.html'

    def form_valid(self, form):
        products_in_cart = ProductInCart.objects.all()
        order = form.save()
        for product in products_in_cart:
            OrderProducts.objects.create(
                product=product.product,
                order=order,
                amount=product.amount
            )
        products_in_cart.delete()
        return redirect('index')
