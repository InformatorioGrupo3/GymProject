from django.views.generic import FormView, RedirectView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.http.response import HttpResponseRedirect


class login_form(FormView):
	form_class = AuthenticationForm
	template_name = 'login.html'
	success_url = reverse_lazy('perfil') # EDITAR LA PLANTILLA

	def form_valid(self, form):
		login(self.request, form.get_user())
		print('INGRESO CON EXITO') # Solo de prueba
		return HttpResponseRedirect(self.success_url)
		
	def form_invalid(self, form):
		print('NO SE PUDO INGRESAR') # Solo de prueba
		return super().form_invalid(form)


class logout_user(RedirectView):
	pattern_name = 'login'

	def dispatch(self, request, *args, **kwargs):
		logout(request)
		return super().dispatch(request, *args, **kwargs)

def perfil(request):
	return HttpResponseRedirect('perfil.html')