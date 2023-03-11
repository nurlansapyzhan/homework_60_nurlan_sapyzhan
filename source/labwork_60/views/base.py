from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from labwork_60.models import Product


def products_view(request: WSGIRequest):
    products = Product.objects.exclude(amount=0).order_by('category', 'title')
    return render(request, 'index.html', context={'products': products})
