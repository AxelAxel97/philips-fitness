from django.shortcuts import render
from .models import Product


def home(request):
    featured_products = Product.objects.all()[:3]
    return render(request, 'shop/home.html', {
        'featured_products': featured_products
    })


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {
        'products': products
    })
