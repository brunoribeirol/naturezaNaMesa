from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

from .models import *

# Create your views here.

@login_required(login_url='login/')   
def naturezaApp(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products':products, 'cartItems': cartItems}
    return render(request, 'naturezaApp/naturezaApp.html', context)

def cart(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'naturezaApp/cart.html', context)

def checkout(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'naturezaApp/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("O item foi adicionado", safe=False)

def entrada(request):
    context = {}
    return render(request, 'naturezaApp/entrada.html', context)

def cadastro(request):
    if request.method=="GET":
        return render(request, 'naturezaApp/cadastro.html')
    else: 
        username=request.POST.get('username')
        email=request.POST.get('email')
        senha=request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse("jÃ¡ existe um usuario com esse username")
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        
        return HttpResponse("usuario cadastrado com sucesso")

def login(request):
    if request.method == "GET":
        return render(request, 'naturezaApp/login.html')
    else: 
        username = request.POST.get('username')
        senha= request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return HttpResponse("autenticado")
        else:
            return HttpResponse("usuario ou senha invalidos")


def plataforma(request):
    if request.user.is_authenticated: 
        return HttpResponse('plataforma')
    return HttpResponse('vc precisa logar')

from django.shortcuts import render, get_object_or_404
from .models import Product

def detalhes_produto(request, product_id):
    produto = get_object_or_404(Product, id=product_id)
    return render(request, 'naturezaApp/detalhes_produto.html', {'produto': produto})
