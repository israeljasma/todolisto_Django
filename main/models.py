from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length = 255)
    descripcion = models.CharField(max_length = 255)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)