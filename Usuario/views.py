from django.shortcuts import render, redirect
from Usuario.models import *
from Usuario.forms import *

def crearUsuario(request):
    titulo_pagina="ciudadano"
    if request.method == 'POST':
        form= CiudadanoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('crear-usuario')
    else:
        form = CiudadanoForm()
    context={
        "titulo_pagina": titulo_pagina,
        "form":form
    }
    return render(request, 'usuarios/crear.html', context)

