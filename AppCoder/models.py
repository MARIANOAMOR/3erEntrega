from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre= models.CharField(max_length=30)
    descripcion= models.CharField(max_length=30)
    precio= models.CharField(max_length=30)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Descripcion {self.descripcion} - Precio {self.precio} "

class Canal(models.Model):
    nombre= models.CharField(max_length=30)
    descripcion= models.CharField(max_length=30)
    campo1= models.CharField(max_length=30)
    campo2= models.CharField(max_length=30)
    campo3= models.CharField(max_length=30)
    campo4= models.CharField(max_length=30)
    campo5= models.CharField(max_length=30)
    campo6= models.CharField(max_length=30)
    campo7= models.CharField(max_length=30)
    campo8= models.CharField(max_length=30)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Descripcion {self.descripcion} - Campo 1 {self.campo1} - Campo 2 {self.campo2} - Campo 3 {self.campo3} - Campo 4 {self.campo4} - Campo 5 {self.campo5} - Campo 6 {self.campo6} - Campo 7 {self.campo7} - Campo 8 {self.campo8}"

class DatosCanal(models.Model):
    campo1= models.FloatField()
    campo2= models.FloatField()
    campo3= models.FloatField()
    campo4= models.FloatField()
    campo5= models.FloatField()
    campo6= models.FloatField()
    campo7= models.FloatField()
    campo8= models.FloatField()
    
    def __str__(self):
        return f"Campo 1: {self.campo1} - Campo 2 {self.campo2} - Campo 3 {self.campo3} - Campo 4 {self.campo4} - Campo 5: {self.campo5} - Campo 6 {self.campo6} - Campo 7 {self.campo7} - Campo 8 {self.campo8}"
"""
class Actuadores(models.Model):
    nombre= models.CharField(max_length=30)
    descripcion= models.CharField(max_length=30)
    campo1= models.EmailField()
    campo2= models.CharField(max_length=30)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Descripcion {self.descripcion} - Campo 1 {self.campo1} - Campo 2 {self.campo2}"
"""
"""
class Curso(models.Model):

    nombre=models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Camada {self.camada}"

class Cliente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    direccion=models.CharField(max_length=30)
    telefono=models.CharField(max_length=30)

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Profesión {self.profesion}"

class Entregable(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField()
"""

