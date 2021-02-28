from django.shortcuts import render, redirect
from .forms import registrar_cliente
from .models import usuario
from django.contrib.auth import login
from django.contrib.auth import logout
from django.views.generic import CreateView
from .models import registro



class login(CreateView):
	model = registro
	form_class = registrar_cliente
	template_name = 'login.html'

def logout_view(request):
    logout(request)

class registro_usuario(CreateView):
	model =usuario
	form_class = registrar_cliente
	template_name = 'registro.html'