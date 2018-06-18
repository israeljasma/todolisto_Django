from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('home', views.index, name='home'),
    path('', views.index, name='home'),
    path('tareas', views.tareas, name='tareas'),
    path('crear_tarea', views.crear_tarea, name='crear_tarea'),
    path('<int:pk>', views.eliminar_tarea, name='eliminar_tarea'),
    path('registrar', views.RegistroUsuario.as_view(), name='registrar'),
    # path('editar_tarea/<int:pk>', views.TareaUpdate.as_view(), name='editar_tarea'),
    path('editar_tarea/<int:pk>', views.actualizarTarea, name='editar_tarea'),
]