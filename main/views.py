
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


def inicio(request):
    titulo_pagina="Inicio"      
    context={
        'titulo_pagina':titulo_pagina,
    }
    return render(request,'inicio.html',context)


def index(request):
    titulo_pagina="Inicio"      
    context={
        'titulo_pagina':titulo_pagina,
    }
    return render(request,'index.html',context)

 
def certificado(request):
    titulo_pagina="Inicio"      
    context={
        'titulo_pagina':titulo_pagina,
    }
    return render(request,'certificado.html',context)          


