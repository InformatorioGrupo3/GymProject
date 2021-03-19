from django.shortcuts import render
from django.views.generic import *
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required


class ver_actividades(ListView):
	model = actividad
	context_object_name = 'lista_actividades'
	template_name = 'actividades.html'

## PRUEBA PARA VER LOS TEMPLATES
# def turno(request):
# 	return render(request,'dashboard.html')


class turnos_actividad(ListView):
	context_object_name = 'lista_turnos'
	template_name = 'ver_turnos.html'
	ordering = ['-horario']
	
	def get_queryset(self):
		query = turno.objects.filter(actividad__nombre=self.kwargs['actividad']).filter(disponible=True)
		return query
	

class ver_turnos_vista(DetailView):
	model = turno
	context_object_name = 'datos_turno'
	template_name = 'prueba.html'


class mis_turnos(ListView):
	model = turno
	context_object_name = 'mis_turnos'
	template_name = 'mis_turnos.html'
	def get_queryset(self):
		tabla_intermedia = turno.usuario.through.objects.all()
		turnos_mios = tabla_intermedia.filter(usuario_id=self.request.user.id)
		lista_ids = []
		for objeto in turnos_mios:
			lista_ids.append(objeto.id)
		query = turno.objects.filter(id__in=lista_ids)
		return query


def solicitar_turno(request):

	return render(request, 'solicitar_turno.html')

