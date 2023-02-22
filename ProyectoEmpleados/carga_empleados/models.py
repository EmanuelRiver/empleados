from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    
    def __str__ (self):
        return self.nombre

class empresa_terciarizada(models.Model):
    nombre = models.CharField(max_length=50)
    razon_social = models.CharField(max_length=50)
    cuit = models.CharField(max_length=50)


