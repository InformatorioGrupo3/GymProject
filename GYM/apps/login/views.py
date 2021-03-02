
from django.shortcuts import render
from apps.registro.models import usuario
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout


# Create your views here.
def login(request):
    user = usuario.objects.get(nombre=request.POST['nombre'])
    user.contraseña == request.POST['contraseña']
    if user.contraseña == request.POST['contraseña']:
        request.session['usuario_id'] = user.id
        return HttpResponse("¡ Bienvenido !", 'index.html')
    else:
        return HttpResponse("Su usuario y contraseña no coinciden.")

def logout_view(request):
    logout(request)
