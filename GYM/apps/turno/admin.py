from django.contrib import admin
from apps.turno.models import *

# Register your models here.

class AdminTurno(admin.ModelAdmin):
    model = turno
    list_display = (
        'id',
        'actividad',
        'fecha',
        'horario',
        'cupo_actual',
        'disponible',
        )
    list_filter = (
        'disponible',
        'actividad',
        )
    readonly_fields = ('cupo_actual',) 

class AdminActividad(admin.ModelAdmin):
    model = actividad
    list_display = (
        'nombre',
        'cupo_max',
        'disponible',
        'descripcion',
        'id',
        )
    list_filter = ('disponible',)

admin.site.register(turno, AdminTurno)
admin.site.register(actividad, AdminActividad)