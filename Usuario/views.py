import re
from django.shortcuts import render, redirect
from Usuario.forms import CiudadanoForm
from Usuario.models import Ciudadano



def crearusuario (request):
    usuarios= Ciudadano.objects.all()
    titulo="Crear usuarios"
    if request.method =='POST':
        form=CiudadanoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request,'usuarios/crear_usuario.html')
    else:
        form=CiudadanoForm
    return redirect(request, 'usuarios/crear_usuario.html')