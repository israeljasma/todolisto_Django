from django.shortcuts import render, redirect
from .models import User, Tarea, EstadoTarea
from .forms import RegistroForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
import time

# Create your views here.
class RegistroUsuario(CreateView):
    model = User
    template_name = 'registration/registro.html'
    form_class = RegistroForm
    success_url = reverse_lazy('login')

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
        tarea.estadoTarea = EstadoTarea.objects.get(pk=request.POST.get('estadoT'))
        tarea.save()
    return redirect('tareas')

@login_required()
def eliminar_tarea(request, pk):
    tarea = Tarea.objects.get(pk=pk)
    tarea.delete()
    return redirect('tareas')