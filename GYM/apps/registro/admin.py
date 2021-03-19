from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import *

# Register your models here.
class administrador(UserAdmin):
    add_form = registrar_usuario
    form = editar_usuario
    model = usuario
    list_display = (
        'username',
        'last_name',
        'first_name',
        'email',
        'dni',
        'fecha_nacimiento',
        'foto',
        #'password',
        'date_joined',
        'is_active',
        'is_staff',
        'is_superuser',
        'id',
    )

admin.site.register(usuario, administrador)