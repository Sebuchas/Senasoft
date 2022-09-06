from multiprocessing import context
from django.shortcuts import render, redirect
from Usuario.models import *
from Usuario.forms import *

def crearUsuario(request):
    titulo_pagina="ciudadano"
    ciudadanos= Ciudadano.objects.all()
    if request.method == 'POST':
        form= CiudadanoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('usuarios-aprendiz')
    else:
        form = CiudadanoForm()
    context={
        "titulo_pagina": titulo_pagina,
        "ciudadanos": ciudadanos,
        "form":form
    }
    return render(request, 'usuarios/crearUsuario.html', context)

