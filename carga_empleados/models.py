from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    
    def __str__ (self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Cargo: {self.cargo}'

class empresa_terciarizada(models.Model):
    nombre = models.CharField(max_length=50)
    razon_social = models.CharField(max_length=50)
    cuit = models.CharField(max_length=50)

    def __str__ (self):
        return f'Nombre: {self.nombre} - Razon Social: {self.razon_social} - Cuit: {self.cuit}'

class vehiculo_empresarial(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    patente = models.CharField(max_length=50)

    def __str__ (self):
        return f'Marca: {self.marca} - Modelo: {self.modelo} - Patente: {self.patente}'
