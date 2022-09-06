from django.urls import path
from Sondeo.views import crearTema, crearPregunta

urlpatterns = [
    path('creartema/', crearTema, name='crear_tema'),
    path('crearpregunta/', crearPregunta, name='crear_pregunta'),
]