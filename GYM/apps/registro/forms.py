
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class registrar_usuario(UserCreationForm):
    class Meta:
        model = usuario
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'dni',
            'fecha_nacimiento',
            'telefono',
            'foto',
        )

class editar_usuario(UserChangeForm):
    class Meta:
        model = usuario
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'dni',
            'fecha_nacimiento',
            'telefono',
            'foto',
        )