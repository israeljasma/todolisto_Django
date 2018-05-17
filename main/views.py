from django.shortcuts import render, redirect
from .models import Tarea
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
    # tareas = Tarea.objects.all()
    return render(request, 'tareas.html', {'tareas' : tareas })

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