from django.shortcuts import render

# Create your views here.

def naturezaApp(request):
    context = {}
    return render(request, 'naturezaApp/naturezaApp.html', context)

def cart(request):
    context = {}
    return render(request, 'naturezaApp/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'naturezaApp/checkout.html', context)



