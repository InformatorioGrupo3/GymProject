from django.contrib import admin
from apps.turno.models import *

# Register your models here.

class AdminTurno(admin.ModelAdmin):
    model = turno
    list_display = ('actividad', 'horario', 'disponible', 'cupo_actual',)
    list_filter = ('disponible',)

class AdminActividad(admin.ModelAdmin):
    model = actividad
    list_display = ('nombre', 'cupo_max', 'disponible', 'descripcion',)
    list_filter = ('disponible',)

admin.site.register(turno, AdminTurno)
admin.site.register(actividad, AdminActividad)