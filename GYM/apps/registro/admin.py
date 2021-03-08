from django.contrib import admin
from apps.registro.models import *

# Register your models here.

class AdminUsuario(admin.ModelAdmin):
    #list_display = ('last_name', 'first_name', 'habilitado', 'dni', 'fecha_nacimiento', 'password',)
    list_display = ('apellido', 'nombre', 'habilitado', 'dni', 'fecha_nacimiento', 'password',)
    list_filter = ('habilitado',)

admin.site.register(usuario, AdminUsuario)