from multiprocessing import context
from django.shortcuts import render, redirect
from Usuario.models import *
from Usuario.forms import *

def crearUsuario(request):
    usuarios= Ciudadano.objects.all()
    titulo="Crear usuarios"
    if request.method =='POST':
        form=CiudadanoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('crear_usuarios')
    else:
        form=CiudadanoForm
    context={
        'usuarios':usuarios,
        'titulo':titulo
    }
    return render(request, 'usuarios/crearUsuario.html', context)

