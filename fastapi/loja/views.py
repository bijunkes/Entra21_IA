from django.shortcuts import render, get_object_or_404
from .models import Cliente, Produto, Venda

# Create your views here.
def menu(request):
    return render(request, 'menu.html')

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def cliente_detalhe(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'cliente_detalhe.html', {'cliente': cliente})

def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})

def vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'vendas.html', {'vendas': vendas})