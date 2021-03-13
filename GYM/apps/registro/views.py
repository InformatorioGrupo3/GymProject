from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import *

class registrar_usuario_vista(CreateView):
    form_class = registrar_usuario
    success_url = reverse_lazy('login')
    template_name = 'registro.html'