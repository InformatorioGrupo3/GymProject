from django.contrib import admin
from apps.turno.models import *

# Register your models here.

class AdminTurno(admin.ModelAdmin):
    model = turno
    list_display = ('actividad', 'horario', 'disponible', 'cupo_actual')

class AdminActividad(admin.ModelAdmin):
    model = actividad
    list_display = ('nombre', 'cupo_max')

admin.site.register(turno, AdminTurno)
admin.site.register(actividad, AdminActividad)