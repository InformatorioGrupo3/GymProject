from django.shortcuts import render
from django.views.generic import *
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

'''
class registro(CreateView):
	model = turno
	form_class = registrar_turno
	template_name = 'turno.html'
'''
'''
def turno_actividad(request):
    return render(request, 'index.html')
'''

class turno_actividad(ListView):
	#model = turno
	context_object_name = 'lista_turnos'
	template_name = 'turno.html'
	ordering = ['-horario']
	
	def get_queryset(self):
		turnos_de_activ = turno.objects.filter(actividad__nombre=self.kwargs['actividad']).filter(disponible=True)
		query = turnos_de_activ
		return query
	

class ver_turnos(ListView):
	model = turno
	context_object_name = 'turnos'
	template_name = 'turno.html'
	
	def get_queryset(self):
		query = turno.objects.filter(disponible=True)
		return query


class ver_actividades(ListView):
	model = actividad
	context_object_name = 'actividades'
	template_name = 'actividad.html'

	def get_queryset(self):
		query = actividad.objects.filter(disponible=True) 
		return query

