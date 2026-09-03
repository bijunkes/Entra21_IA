from django.shortcuts import render
from .models import Artistas

# Create your views here.
def index(request):
    artistas = Artistas.objects.all()
    return render(request, 'index.html', {'artistas': artistas})

def ver_artista(request, artista_id):
    artistas = Artistas.objects.filter(id = artista_id)
    return render(request, 'index.html', {'artistas': artistas})