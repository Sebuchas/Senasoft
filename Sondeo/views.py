from django.shortcuts import render, redirect
from Sondeo.models import *
from Sondeo.forms import *
from django.contrib import messages

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

def crearPregunta(request,pk):
    titulo_pagina="facturas"
    pregunta= Pregunta.objects.filter(idSondeo_id=pk)
    sondeo_u=Sondeo.objects.get(id=pk)
    if request.method == 'POST':
        form= PreguntaForm(request.POST)
        if form.is_valid():
            Pregunta.objects.create(                                                          
                    sondeo=sondeo_u,               
            )
            return redirect('sondeo-preguntas', pk=pk)
        else:
            pass
    else:
        form= PreguntaForm() 
    context={
        "titulo_pagina": titulo_pagina,
        "pregunta": pregunta,                                   
        "form":form,
        "sondeo":sondeo_u,
    }
    return render(request, "sondeos/crear-preguntas.html", context)

def crearSondeo(request):
    titulo_pagina="sondeo"
    sondeos = Sondeo.objects.all()
    parametros = ParametroForm()
    titulo = "Sondeo"
    if request.method == 'POST':
        parametros = ParametroForm(request.POST)
        form= SondeoForm(request.POST, request.FILES)
        if form.is_valid():
            fechaApertura= form.cleaned_data.get('fechaApertura')
            fechaCierre=form.cleaned_data.get('fechaCierre')
            if (fechaApertura <= fechaCierre):
                form.save()
            else:
                messages.warning (request,f' Error las fechas estan mal!!!')
            
            
        return redirect('crear_sondeo')
    else:
        form = SondeoForm()
    context={
        "titulo_pagina": titulo_pagina,
        "form":form,
        "sondeos":sondeos,
        "titulo":titulo,
        "parametros":parametros
    }
    return render(request, 'pag-admin.html', context)



def crearParametro(request, pk):
    titulo_pagina="pregunta"
    if request.method == 'POST':
        form= ParametroForm(request.POST)
        if form.is_valid():
            form.save()
            print("XDDDDDDDDD")
        return redirect('parametro.html')
    else:
        form = ParametroForm()
    context={
        "titulo_pagina": titulo_pagina,
        "form":form
    }
    return render(request, 'parametro.html', context)

