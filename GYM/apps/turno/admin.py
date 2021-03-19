from django.contrib import admin
from apps.turno.models import *

# Register your models here.

class AdminTurno(admin.ModelAdmin):
    model = turno
    list_display = (
        'nombre',
        'actividad',
        'fecha',
        'horario',
        #'cupo_actual',
        'disponible',
        'id',
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
        'nombre_corto',
        'cupo_max',
        'disponible',
        'descripcion',
        'id',
        )
    list_filter = ('disponible',)

admin.site.register(turno, AdminTurno)
admin.site.register(actividad, AdminActividad)