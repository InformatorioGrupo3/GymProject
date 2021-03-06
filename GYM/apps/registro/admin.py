from django.contrib import admin
from apps.registro.models import *

# Register your models here.

class AdminUsuario(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'habilitado', 'dni', 'fecha_nacimiento',)
    list_filter = ('habilitado',)

admin.site.register(usuario, AdminUsuario)