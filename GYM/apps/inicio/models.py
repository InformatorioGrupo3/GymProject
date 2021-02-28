from django.db import models
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='inicio')
def inicio(request):
    return render(request, 'inicio.html') # Agregar HTML de perfil para cuando inicia sesion
