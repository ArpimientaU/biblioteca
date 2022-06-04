from django.db import models
from apps.libros.models import Libro

# Create your models here.

class Usuario (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Ejemplar(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, null=True, blank=True)
    localizacion = models.CharField(max_length=30)
    usuario = models.ManyToManyField(Usuario, through="Prestar")

    def __str__(self):
        return self.localizacion

class Prestar(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    ejemplar = models.ForeignKey(Ejemplar, on_delete=models.CASCADE, blank=True, null=True)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()

    def __str__(self):
        return self.fecha_prestamo