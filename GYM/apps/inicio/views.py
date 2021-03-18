from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='inicio')
def perfil(request):
    return render(request, 'perfil.html') 


def inicio(request):
	return render(request, 'index.html')

def contacto(request):
	return render(request, 'contacto.html')

def informacion(request):
	return render(request, 'informacion.html')

