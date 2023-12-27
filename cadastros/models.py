from django.db import models

# Create your models here.

class Cachaca(models.Model):
    nome = models.CharField(max_length=100)
    ano_fabricacao = models.DateField()
    foto_thumb = models.ImageField()
    foto_ilust = models.ImageField()
    origem = models.BooleanField()


class CidadeFabricacao(models.Model):
    nome = models.CharField(max_length=255)
    estado = models.CharField(max_length=100)
    cep = models.IntegerField(max_length=8)
    
