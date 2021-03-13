from django.shortcuts import render
from django.views.generic import *
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required


class turno_actividad(ListView):
	#model = turno
	context_object_name = 'lista_turnos'
	template_name = 'turno.html'
	ordering = ['-horario']
	
	def get_queryset(self):
		query = turno.objects.filter(actividad__nombre=self.kwargs['actividad']).filter(disponible=True) 
		return query
	

class ver_turnos(ListView):
	model = turno
	template_name = 'turno.html'


class ver_actividades(ListView):
	model = actividad
	template_name = 'actividad.html'

## PRUEBA PARA VER LOS TEMPLATES
# def turno(request):
# 	return render(request,'dashboard.html')

# def solicitar_turno(request):
# 	return render(request,'call_solicitud.html')
