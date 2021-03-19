from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(ver_turnos_vista.as_view()), name='turno'),
    path('mis-turnos/', login_required(mis_turnos.as_view()), name='mis-turnos'),
    path('actividades/', login_required(ver_actividades.as_view()), name='actividades'),
    path('<str:actividad>/', login_required(turnos_actividad.as_view()), name='turnos_actividad'),
    path('<str:actividad>/<int:turno_id>/', login_required(ver_turnos_vista.as_view()), name='ver_turnos'),

    #path('turno/', views.turno, name='turno'),
	path('solicitar_turno/', login_required(solicitar_turno), name='solicitar_turno'),
]