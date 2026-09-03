from django.contrib import admin
from .models import Artistas

# Register your models here.
# admin.site.register(Artistas)

@admin.register(Artistas)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'pais', 'data_nascimento', 'avaliacao', 'data_cadastro']
    search_fields = ['nome', 'pais']
    list_filter = ['data_cadastro']