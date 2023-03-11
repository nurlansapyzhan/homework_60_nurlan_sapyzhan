from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404, render, redirect

from labwork_60.forms import ProductForm
from labwork_60.models import Product


def product_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', context={'product': product})


def add_product_view(request: WSGIRequest):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'add_product.html', context={'form': form})
    form = ProductForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'add_product.html', context={'form': form})
    else:
        Product.objects.create(**form.cleaned_data)
        return redirect('index')


def delete_product(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_delete_confirm.html', context={'product': product})


def confirm_delete(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('index')


def edit_product(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            'title': product.title,
            'description': product.description,
            'image': product.image,
            'category': product.category,
            'amount': product.amount,
            'price': product.price
        })
        return render(request, 'product_edit.html', context={'product': product, 'form': form})
    form = ProductForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'product_edit.html', context={'product': product, 'form': form})
    else:
        product.title = request.POST.get('title')
        product.description = request.POST.get('description')
        product.image = request.POST.get('image')
        product.category = request.POST.get('category')
        product.amount = request.POST.get('amount')
        product.price = request.POST.get('price')
        product.save()
        return redirect('index')
