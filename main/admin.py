from django.contrib import admin
from .models import Tarea, EstadoTarea, TipoTarea

# Register your models here.
admin.site.register(Tarea)
admin.site.register(EstadoTarea)
admin.site.register(TipoTarea)
