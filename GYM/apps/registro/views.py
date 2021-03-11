from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import registrar_cliente

class registrar_cliente_vista(CreateView):
    form_class = registrar_cliente
    success_url = reverse_lazy('login')
    template_name = 'registro.html'


'''
from django.shortcuts import render, redirect
from .forms import registrar_cliente
from .models import *
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

@login_required
def registro(request):
	return registrar_cliente

class registro_usuario(CreateView):
	model = cliente
	form_class = registrar_cliente
	template_name = 'registro.html'
'''