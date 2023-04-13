from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class cliente(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True)
    nombre = models.CharField(max_length=50)
    telefono= models.CharField(max_length=10)
    direccion=models.CharField(max_length=50)
    correo=models.CharField(max_length=50)

    def __str__(self) :
        return self.nombre
   




class Activdades_fisicas(models.Model): 
    nombre=models.CharField(max_length=50)
    descipcion=models.CharField(max_length=50) 
    act_usu=models.ManyToManyField(cliente)

    def __str__(self) :
        return self.nombre


class Pausas_Activas(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_inicio=models.DateTimeField()
    fecha_fin=models.DateTimeField()
    duracion=models.CharField(max_length=10)
    descripcion=models.CharField(max_length=500)
    cliente=models.ForeignKey(cliente,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self) :
        return self.nombre
    




