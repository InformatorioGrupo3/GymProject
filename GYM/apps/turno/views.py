from django.shortcuts import render
from django.views.generic import *
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
import datetime


class ver_actividades(ListView):
    model = actividad
    context_object_name = 'lista_actividades'
    template_name = 'actividades.html'
    queryset = actividad.objects.filter(disponible=True)

## PRUEBA PARA VER LOS TEMPLATES
# def turno(request):
# 	return render(request,'dashboard.html')


class fechas_por_actividad(ListView):
    model = turno
    context_object_name = 'lista_turnos'
    template_name = 'ver_fechas.html'

    def get_queryset(self):
        query = turno.objects \
            .filter(actividad__nombre=self.kwargs['actividad']) \
            .filter(fecha__gte=datetime.datetime.today()) \
            .filter(horario__gte=datetime.datetime.now())

        lista_fechas = []
        lista_turnos = []
        for turno1 in query:
            if turno1.fecha not in lista_fechas:
                lista_fechas.append(turno1.fecha)
                lista_turnos.append(turno1)
        return lista_turnos


class ver_horarios(ListView):
    model = turno
    context_object_name = 'lista_turnos'
    template_name = 'ver_horarios.html'

    def get_queryset(self):
        query = turno.objects \
            .filter(actividad__nombre=self.kwargs['actividad']) \
            .filter(fecha=self.kwargs['turno_fecha']) \
            .filter(fecha__gte=datetime.datetime.today()) \
            .filter(horario__gte=datetime.datetime.now())

        lista_horarios = []
        lista_turnos = []
        for turno1 in query:
            if turno1.horario not in lista_horarios:
                lista_horarios.append(turno1.horario)
                lista_turnos.append(turno1)
        return lista_turnos


class mis_turnos(ListView):
    model = turno
    context_object_name = 'mis_turnos'
    template_name = 'mis_turnos.html'

    def get_queryset(self):
        tabla_intermedia = turno.usuario.through.objects.all()
        turnos_mios = tabla_intermedia.filter(usuario_id=self.request.user.id)
        lista_ids = []
        for objeto in turnos_mios:
            lista_ids.append(objeto.turno_id)
        query = turno.objects.filter(id__in=lista_ids)
        return query


class prueba(ListView):
    model = turno
    context_object_name = 'prueba'
    template_name = 'prueba.html'

    def get_queryset(self):
        query = turno.objects \
            .filter(actividad__cupo_max__gte=3)
        return query


def solicitar_turno(request):
    return render(request, 'solicitar_turno.html')
