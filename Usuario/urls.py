from django.urls import path
from Usuario.views import crearusuario

urlpatterns = [
    path('crearusuario',crearusuario, name='crear_usuario'),
]