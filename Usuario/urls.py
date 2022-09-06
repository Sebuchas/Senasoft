from django.urls import path
from Usuario.views import *

urlpatterns = [
    path('crearusuario/', crearUsuario, name='crear_usuario'),
]