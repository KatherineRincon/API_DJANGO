from django.db import models

# Create your models here.
#aqui se crean los modelos (las tablas o colecciones)

class programmer(models.Model):
    fullname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField(default=True)
    Cellphone = models.CharField(max_length=10, null=True, default=None)
    is_active =models.BooleanField(default=True)
    
class Student(models.Model):
    nombre = models.CharField(max_length=20)    
    apellido = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1)
    numero_ficha = models.PositiveSmallIntegerField(max_length=7)
    formacion = models.BooleanField(default=True)
    fecha_ingreso = models.DateField()
    
    