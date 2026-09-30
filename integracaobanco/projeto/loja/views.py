from django.shortcuts import render, redirect, get_list_or_404
from .models import Produto, Categoria
from .forms import ProdutoForm, CategoriaForm

# --------------------------
# PRODUTOS
# --------------------------
def listar_produtos(request):
    produtos = Produto.objects.all()
    
    return render(request, 'lista_produtos.html', {'produtos': produtos})

# --------------------------
# CATEGORIAS
# --------------------------
def listar_categorias(request):
    categorias = Categoria.objects.all()
    
    return render(request, 'lista_categorias.html', {'categorias': categorias})

def cadastrar_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('listar_categorias')
    else:
        form = CategoriaForm()
        return render(request, 'cadastrar_categoria.html', {'form': form})