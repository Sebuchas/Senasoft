from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


def registrar(request, pk):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)	
		if form.is_valid() :	
			form.save()
			username = form.cleaned_data['username']
			
			messages.success(request, f'Usuario {username} creado correctamente')
			return redirect('datos-usuario')
	else:
		form = UserRegisterForm()
	context = { 'form' : form,
	}	
	return render(request, 'user/registrar.html', context)




