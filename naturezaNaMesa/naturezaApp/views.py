from django.shortcuts import render
from .models import *

# Create your views here.

def naturezaApp(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'naturezaApp/naturezaApp.html', context)

def cart(request):
    context = {}
    return render(request, 'naturezaApp/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'naturezaApp/checkout.html', context)

def main(request):
    context = {}
    return render(request, 'naturezaApp/main.html', context)

