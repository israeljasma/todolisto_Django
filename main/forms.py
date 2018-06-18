from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import Tarea
import time

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
        }

class TareaCreateForm(forms.ModelForm):
    titulo = forms.CharField()
    descripcion = forms.CharField()
    usuario = User
    fechaInicio = time.strftime("%Y-%m-%d")
    fechaTermino = forms.DateField()

    class Meta:
            model = Tarea
            fields = ('titulo', 'descripcion', 'fechaTermino')