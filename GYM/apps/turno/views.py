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
		query = turno.objects.filter(actividad__nombre=self.kwargs['actividad']).filter(disponible=True) 
		return query
	

class ver_turnos(ListView):
	model = turno
	template_name = 'turno.html'


class ver_actividades(ListView):
	model = actividad
	template_name = 'actividad.html'

