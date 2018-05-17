from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length = 255)
    descripcion = models.CharField(max_length = 255)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    fechaInicio = models.DateField("%d-%m-%Y")
    fechaTermino = models.DateField("%d-%m-%Y", null=True, blank=True)

class EstadoTarea(models.Model):
    Estado = models.CharField(max_length = 255)

class TipoTarea(models.Model):
    Tipo = models.CharField(max_length = 255)