from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('home', views.index, name='home'),
    path('', views.index, name='home'),
    path('tareas', views.tareas, name='tareas'),
    path('creartarea', views.crear_tarea, name='crear_tarea'),
    path('<int:pk>', views.TareaDelete.as_view(), name='eliminar_tarea'),
    path('register', views.RegistroUsuario.as_view(), name='register'),
    # path('editar_tarea/<int:pk>', views.TareaUpdate.as_view(), name='editar_tarea'),
    path('editartarea/<int:pk>', views.actualizarTarea, name='editar_tarea'),
    path('calendario', views.calendario, name='calendario'),
    path('detallestarea/<int:pk>', views.TareaDetail.as_view(), name='detalles_tarea'),
]