from django.shortcuts import render
from django.views.generic import CreateView
#from .forms import registrar_turno

# class registro(CreateView):
# 	model = turno
# 	form_class = registrar_turno
# 	template_name = 'turno.html'


def turno(request):
	return render(request,'dashboard.html')

def solicitar_turno(request):
	return render(request,'call_solicitud.html')

