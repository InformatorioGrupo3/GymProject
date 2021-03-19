from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(ver_horarios.as_view()), name='turno'),
    path('mis-turnos/', login_required(mis_turnos.as_view()), name='mis-turnos'),
    path('prueba/', login_required(prueba.as_view()), name='prueba'),
    path('actividades/', login_required(ver_actividades.as_view()), name='actividades'),
    path('<actividad>/', login_required(fechas_por_actividad.as_view()), name='fechas_por_actividad'),
    path('<actividad>/<turno_fecha>/', login_required(ver_horarios.as_view()), name='ver_horarios'),
    path('<actividad>/<turno_fecha>/<turno_id>/',
         login_required(ver_horarios.as_view()),
         name='info_turno'
         ),

    #path('turno/', views.turno, name='turno'),
	path('solicitar_turno/', login_required(solicitar_turno), name='solicitar_turno'),
]