from django.urls import path
from Sondeo.views import *

urlpatterns = [
    path('creartema/', crearTema, name='crear_tema'),
    path('crearpregunta/', crearPregunta, name='crear_pregunta'),
    path('crearsondeo/', crearSondeo, name='crear_sondeo'),
    path('parametro/<int>', crearParametro, name='crear_parametro'),
    # path('certificacion/<int>', certificacion, name='certificacion'),
]