from django.shortcuts import render, redirect
from Sondeo.models import *
from Sondeo.forms import *

def crearTema(request):
    titulo_pagina="tema"
    if request.method == 'POST':
        form= TemaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('crear_tema')
    else:
        form = TemaForm()
    context={
        "titulo_pagina": titulo_pagina,
        "form":form
    }
    return render(request, 'crear.html', context)

def crearPregunta(request):
    titulo_pagina="pregunta"
    if request.method == 'POST':
        form= PreguntaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('crear_pregunta')
    else:
        form = PreguntaForm()
    context={
        "titulo_pagina": titulo_pagina,
        "form":form
    }
    return render(request, 'crear.html', context)

def crearSondeo(request):
    titulo_pagina="sondeo"
    sondeos = Sondeo.objects.all()
    if request.method == 'POST':
        form= SondeoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('crear_sondeo')
    else:
        form = SondeoForm()
    context={
        "titulo_pagina": titulo_pagina,
        "form":form,
        'sondeos':sondeos
    }
    return render(request, 'pag-admin.html', context)

def crearParametro(request, pk):
    titulo_pagina="pregunta"
    if request.method == 'POST':
        form= ParametroForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('crear-usuario')
    else:
        form = ParametroForm()
    context={
        "titulo_pagina": titulo_pagina,
        "form":form
    }
    return render(request, 'crear.html', context)

