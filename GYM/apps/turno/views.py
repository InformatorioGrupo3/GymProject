from django.shortcuts import render
from django.views.generic import CreateView
from .forms import registrar_turno
from .models import turno

class registro(CreateView):
	model = turno
	form_class = registrar_turno
	template_name = 'turno.html'
	