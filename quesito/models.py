from django.db import models
from django import forms

# Create your models here.
    
class registro (models.Model):
    correo      = models.TextField(max_length=120)
    nombre      = models.TextField(max_length=120)
    contraseña  = models.TextField(max_length=120)
   
    def __str__ (self):
        return self.nombre

class Productos(models.Model):
    nombrep     = models.TextField(max_length=120)
    descripcion = models.TextField(max_length=280)
    img         = models.ImageField(upload_to = "imagenes/")
    stock 		= models.IntegerField(null=True)
    precioCosto = models.IntegerField(null=True)
    precioVenta	= models.IntegerField(null=True)
    def __str__ (self):
        return self.nombrep