from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import *

# Register your models here.
class administrador(UserAdmin):
    add_form = registrar_cliente
    form = editar_cliente
    model = cliente
    list_display = (
        'last_name',
        'first_name',
        'username',
        'email',
        'dni',
        'fecha_nacimiento',
        'password',
        'date_joined',
        'is_active',
        'is_staff',
        'is_superuser',
    )

admin.site.register(cliente, administrador)

'''
class AdminUsuario(admin.ModelAdmin):
    #list_display = ('last_name', 'first_name', 'habilitado', 'dni', 'fecha_nacimiento', 'password',)
    list_display = (
        'apellido',
        'nombre',
        'habilitado',
        'dni',
        'fecha_nacimiento',
        'password',
        'fecha_ingreso',
        )
    list_filter = ('habilitado',)

admin.site.register(usuario, AdminUsuario)
'''

'''
class AdminCliente(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'username',
        'dni',
        'fecha_nacimiento',
        'password',
        'date_joined',
        'is_active',
        'is_staff',
        'is_superuser',
        )
    list_filter = ('is_active',)

admin.site.register(cliente, AdminCliente)
'''