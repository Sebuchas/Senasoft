from django.shortcuts import render, redirect
from Sondeo.models import *
from Sondeo.forms import *

def crearTema(request):
    titulo_pagina="tema"
    if request.method == 'POST':
        form= TemaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('crear-usuario')
    else:
        form = TemaForm()
    context={
        "titulo_pagina": titulo_pagina,
        "form":form
    }
    return render(request, 'usuarios/crear.html', context)

def crearPregunta(request):
    titulo_pagina="pregunta"
    if request.method == 'POST':
        form= PreguntaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('crear-usuario')
    else:
        form = PreguntaForm()
    context={
        "titulo_pagina": titulo_pagina,
        "form":form
    }
    return render(request, 'usuarios/crear.html', context)

