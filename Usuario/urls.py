from django.urls import path
from Usuario.views import *

urlpatterns = [
    path('datospersonales/<int:pk>/', datosUsuario, name='datos_usuario'),
]