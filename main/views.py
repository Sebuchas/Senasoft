
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.views.generic import CreateView, TemplateView

from .models import Perfil
from django.contrib.auth.views import LoginView, LogoutView 
from .forms import SignUpForm


from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
   template_name = 'login/bienvenida.html'



class SignInView(LoginView):
    template_name = 'login/ingreso.html'
    


class SignOutView(LogoutView):
    pass


def inicio(request):
    titulo_pagina="Inicio"      
    context={
        'titulo_pagina':titulo_pagina,
    }
    if 'ingreso':
        print('Holiwipigui')
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