from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from cuenta.models import *
from django.contrib.auth.models import User

def registrar(request):
	register= Postt.objects.all(
	)
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)	
		if form.is_valid() :	
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado correctamente')
			return redirect('datos_usuario')
	else:
		form = UserRegisterForm()
	context = { 'form' : form,
            	'register':register
	}	
	return render(request, 'user/registrar.html', context)




