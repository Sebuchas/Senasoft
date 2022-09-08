
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


def inicio(request):
    titulo_pagina="Inicio"
    titulo = "Sondeo"
    context={
        'titulo_pagina':titulo_pagina,
        'titulo':titulo,    }
    if 'ingreso':
        print('Holiwipigui')
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

def export_pdf(request):

    context = {}
    html = render_to_string("report/report-pdf.html", context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; report.pdf"

    font_config = FontConfiguration()
    HTML(string=html).write_pdf(response, font_config=font_config)

    return response
