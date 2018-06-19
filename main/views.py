from django.shortcuts import render, redirect
from .models import User, Tarea, EstadoTarea, TipoTarea
from .forms import RegistroForm, TareaUpdateForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import time

#decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class RegistroUsuario(CreateView):
    model = User
    template_name = 'registration/registro.html'
    form_class = RegistroForm
    success_url = reverse_lazy('login')

class TareaUpdate(UpdateView):
    model = Tarea
    form_class = TareaUpdateForm
    template_name = 'editar_tarea.html'
    success_url = reverse_lazy('tareas')

@method_decorator(login_required, name='get')
class TareaDelete(DeleteView):
    model = Tarea
    template_name = 'tareas.html'
    success_url = reverse_lazy('tareas')

@login_required()
def index(request):
    return render(request, 'home.html')

@login_required()
def tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    estadoTarea = EstadoTarea.objects.all()
    tipoTarea = TipoTarea.objects.all()
    context = {'tareas' : tareas, 'estadoTarea' : estadoTarea, 'tipoTarea': tipoTarea}
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
def actualizarTarea(request, pk):
    tarea = Tarea.objects.get(pk=pk)
    if request.method == 'GET':
        form = TareaUpdateForm(instance=tarea)
    else:
        form = TareaUpdateForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
        return redirect('tareas')
    return render(request, 'editar_tarea.html', {'form':form})