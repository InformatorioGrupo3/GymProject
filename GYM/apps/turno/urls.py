from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

# Configuración URL de la app registro
# Si agrego funciones en la view de la app registro debo agregar los path acá
urlpatterns = [
    path('', login_required(ver_actividades.as_view()), name='turnos'),
    path('actividad/', login_required(ver_turnos.as_view()), name='actividad'),
    path('<actividad>/', login_required(turno_actividad.as_view()), name='turno_actividad'),
    path('<actividad>/<id_turno>', login_required(ver_turnos.as_view())),
]