from django.shortcuts import render
from django.views.generic import CreateView
from .forms import registrar_turno
from .models import turno
from django.contrib.auth.decorators import login_required

class registro(CreateView):
	model = turno
	form_class = registrar_turno
	template_name = 'turno.html'

@login_required
class turnos_views(CreateView):
	template_name = 'solicitar_turno.html'
	form_class = registrar_turno

	def turno(self, request):
		return render(request,'dashboard.html')

@login_required
def solicitar_turno(request):
	return render(request,'call_solicitud.html')

