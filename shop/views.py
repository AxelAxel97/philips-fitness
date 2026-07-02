from django.shortcuts import render

def home(request):
    return render(request, 'shop/home.html')

def product_list(request):
    return render(request, 'shop/product_list.html')
