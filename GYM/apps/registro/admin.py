from django.contrib import admin
from apps.registro.models import usuario

# Register your models here.

class AdminUsuario(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'habilitado', 'dni', 'fecha_nacimiento')

admin.site.register(usuario, AdminUsuario)


