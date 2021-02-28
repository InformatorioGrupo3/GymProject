from django.shortcuts import render, redirect
from .forms import registrar_cliente
from .models import usuario
from django.views.generic import CreateView

def registro(request):
	return registrar_cliente

class registro_usuario(CreateView):
	model = usuario
	form_class = registrar_cliente
	template_name = 'registro.html'