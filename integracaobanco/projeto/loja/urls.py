from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/cadastrar', views.cadastrar_categoria, name='cadastrar_categoria'),
]