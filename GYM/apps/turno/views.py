from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import registrar_turno
from .models import turno

class crear_turno(CreateView):
	model = turno
	form_class = registrar_turno
	template_name = 'turno.html'
	
class modificar_turno(UpdateView):
	model = turno
	form_class = registrar_turno
	template_name = 'turno.html'

	