from django.shortcuts import render, redirect
from .models import Tarea, EstadoTarea
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import time

# Create your views here.
@login_required()
def index(request):
    return render(request, 'home.html')

@login_required()
def tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    estadoTarea = EstadoTarea.objects.all()
    context = {'tareas' : tareas, 'estadoTarea' : estadoTarea}
    # tareas = Tarea.objects.all()
    return render(request, 'tareas.html', context=context)

@login_required()
def crear_tarea(request):
    if request.method == 'POST':
        tarea = Tarea()
        tarea.titulo = request.POST.get('titulo_tarea')
        tarea.descripcion = request.POST.get('descripcion_tarea')
        tarea.usuario = request.user
        tarea.fechaInicio = time.strftime("%Y-%m-%d")
        tarea.save()
    return redirect('tareas')