from django.shortcuts import render, redirect
from apps.registro.forms import registrar_cliente
from apps.registro.models import usuario
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.views.generic import CreateView


class login(CreateView):
	model = usuario
	form_class = registrar_cliente
	template_name = 'login.html'

def logout_view(request):
    logout(request)