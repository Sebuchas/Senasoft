from django.urls import path
from Usuario.views import *

urlpatterns = [
    path('datospersonales/', datosUsuario, name='datos_usuario'),
]