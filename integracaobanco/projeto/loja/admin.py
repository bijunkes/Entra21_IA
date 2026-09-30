from django.contrib import admin
from .models import Categoria, Produto

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_filter = ['nome']
    search_fields = ['nome']
    
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'preco', 'categoria']
    list_filter = ['id', 'nome', 'preco', 'categoria']
    search_fields = ['id', 'nome', 'preco', 'categoria']