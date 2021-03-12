from django.shortcuts import render, redirect
from .forms import registrar_cliente
from .models import usuario
from django.views.generic import CreateView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

@login_required
def registro(request):
	data = {
		'form' : registrar_cliente()
	}
	if request.method == 'POST':
		nuevo_user = registrar_cliente(data = request.POST)
		if nuevo_user.is_valid():
			nuevo_user.save()
			user = authenticate(username=nuevo_user.cleaned_data["email"], password=nuevo_user.cleaned_data["password1"])
			login(request, user)
			messages.success(request, "¡ Se ha registrado con éxito !")
			return redirect(to='perfil')
		data['form'] = nuevo_user

	return render(request, 'registro.html', data)


class registro_usuario(CreateView):
	model = usuario
	form_class = registrar_cliente
	template_name = 'registro.html'
