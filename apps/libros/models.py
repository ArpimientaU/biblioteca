from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    editorial = models.CharField(max_length=30)
    numero_pagina = models.CharField(max_length=30)
    isbn = models.CharField(max_length=30)
    autor=models.ForeignKey(Autor, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.titulo