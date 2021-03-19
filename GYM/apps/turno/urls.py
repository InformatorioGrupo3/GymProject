from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(ver_horarios.as_view()), name='turno'),
    path('mis-turnos/', login_required(mis_turnos.as_view()), name='mis-turnos'),
    path('actividades/', login_required(ver_actividades.as_view()), name='actividades'),
    path('sacar_turno/<turno_id>/<usuario_id>/', login_required(sacar_turno.as_view()), name='sacar_turno'),

    path('<actividad>/', login_required(fechas_por_actividad.as_view()), name='fechas_por_actividad'),
    path('<actividad>/<turno_fecha>/', login_required(ver_horarios.as_view()), name='ver_horarios'),
    path('<actividad>/<turno_fecha>/<int:pk>/',
         login_required(info_turno.as_view()),
         name='info_turno'
         ),

]