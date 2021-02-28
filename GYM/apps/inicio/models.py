from django.db import models
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='inicio')
def perfil(request):
    return render(request, 'perfil.html') # Agregar HTML de perfil para cuando inicia sesion
