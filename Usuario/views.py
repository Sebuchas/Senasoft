from django.shortcuts import render, redirect
from Usuario.models import *
from Usuario.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url="usuario-login")
def datosUsuario(request, pk):
    registros = CiudadanoForm.objects.all()
    registros_obj = Ciudadano.objects.get(id=pk)
    if request.method == 'POST':
        form = CiudadanoForm(request.POST)
        if form.is_valid():
            Ciudadano.objects.filter(id=pk).update(
                correo=form.cleaned_data.get('correo'),
            )
        return redirect('index')
    else:
        form = CiudadanoForm()

    context = {
        'registros': registros,
        "form": form,
    }
    return render(request, "user/registrar.html", context)