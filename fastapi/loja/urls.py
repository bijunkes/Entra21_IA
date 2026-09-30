from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/<int:id>/', views.cliente_detalhe, name='cliente_detalhe'),
    path('produtos/', views.produtos, name='produtos'),
    path('vendas/', views.vendas, name='vendas')
]