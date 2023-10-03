from django.urls import path
from . import views

urlpatterns = [
    path('', views.naturezaApp, name='naturezaApp'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

    path('entrada/', views.entrada, name='entrada'),
    path('produto/<int:product_id>/', views.detalhes_produto, name='detalhes_produto'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),

    path('update_item/', views.updateItem, name='update_item')
]
