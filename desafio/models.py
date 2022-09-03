from operator import mod
from django.db import models

# Create your models here.
class Usuario(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.name


class Lista(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    item_filho = models.ForeignKey(
        "Item", null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name
