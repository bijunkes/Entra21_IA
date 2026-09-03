from django.db import models

# Create your models here.
class Artistas(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    avaliacao = models.IntegerField()
    
    def __str__(self):
        return self.nome