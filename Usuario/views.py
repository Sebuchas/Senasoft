import re
from django.shortcuts import render
from Usuario.models import Models


def crearusuario (request):
    usuarios= Models.Ciudadano.objects.all()
    titulo="Crear usuarios"
    if request.method =='POST':
        form=Clienteform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=Clienteform
    return redirect(request, '')