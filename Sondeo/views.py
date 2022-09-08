from datetime import datetime
from django.shortcuts import render, redirect
from Sondeo.models import *
from Sondeo.forms import *
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime

@login_required(login_url="usuario-login")
@permission_required('is_superuser')
def crearTema(request):
    titulo_pagina="tema"
    if request.method == 'POST':
        form= TemaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('crear_sondeo')
    else:
        form = TemaForm()
    context={
        "titulo_pagina": titulo_pagina,
        "form":form
    }
    return render(request, 'admin/crear.html', context)

@login_required(login_url="usuario-login")
@permission_required('is_superuser')
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
    return render(request, 'admin/crear.html', context)

@login_required(login_url="usuario-login")
@permission_required('is_superuser')
def crearSondeo(request):
    fecha = datetime.today().strftime('%d-%m-%Y')
    titulo_pagina="sondeo"
    sondeos = Sondeo.objects.all()
    titulo = "Sondeo"
    parametros = ParametroForm()
    if request.method == 'POST':
        form= SondeoForm(request.POST, request.FILES)
        parametros = ParametroForm(request.POST)
        if form.is_valid():
            fechaApertura = form.cleaned_data.get('fechaApertura')
            fechaCierre = form.cleaned_data.get('fechaCierre')
            if (fechaApertura<=fechaCierre):
                form.save()
            else:
                form = SondeoForm()
        return redirect('crear_sondeo')
    else:
        form = SondeoForm()
    context={
        "titulo_pagina": titulo_pagina,
        "form":form,
        "sondeos":sondeos,
        "titulo":titulo,
        "parametros":parametros,
        "fecha":fecha
    }
    return render(request, 'admin/pag-admin.html', context)

@login_required(login_url="usuario-login")
@permission_required('is_superuser')
def crearParametro(request, pk):
    titulo_pagina="pregunta"
    if request.method == 'POST':
        form= ParametroForm(request.POST)
        if form.is_valid():
            form.save()
            print("XDDDDDDDDD")
        return redirect('crear_parametro')
    else:
        form = ParametroForm()
    context={
        "titulo_pagina": titulo_pagina,
        "form":form
    }
    return render(request, 'admin/crear.html', context)

def crearCertificado(request, pk, kp):
    radicado = random.randint(start, end)