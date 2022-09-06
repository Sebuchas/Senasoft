from django.shortcuts import render
from Usuario.models import Models

def crearusuario (request):
    usuarios= Models.Ciudadano.objects.all()
    return render(request, '')