from django.shortcuts import render, redirect
from Usuario.models import *
from Usuario.forms import *
from django.contrib.auth.models import User

def datosUsuario(request, pk):
    datos= Ciudadano.objects.filter(idUser_id=pk)
    user=User.objects.get(id=pk)

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
        "form":form,
        "datos":datos,
        "user":user
    }
    return render(request, 'usuarios/crear.html', context)

