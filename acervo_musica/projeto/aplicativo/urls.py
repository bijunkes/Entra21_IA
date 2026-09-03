from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artistas/<int:artista_id>', views.ver_artista, name='ver_artista')
]