from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import *
from .models import *

class registrar_usuario_vista(CreateView):
	model = usuario
	form_class = registrar_usuario
	success_url = reverse_lazy('login')
	template_name = 'registro.html'

class editar_usuario_vista(UpdateView):
	model = usuario
	form_class = editar_usuario
	success_url = reverse_lazy('perfil')
	template_name =	'editar_perfil.html'
	