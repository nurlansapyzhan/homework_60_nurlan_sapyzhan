from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from labwork_60.forms import ProductForm
from labwork_60.models import Product


class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    model = Product


class ProductCreateView(CreateView):
    template_name = 'add_product.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    template_name = 'product_edit.html'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'product_delete_confirm.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('index')
