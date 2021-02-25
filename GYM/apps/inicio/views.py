from django.shortcuts import render

# Create your views here.
def inicio(request):
	return render(request, 'index.html')

def contacto(request):
	return render(request, 'contacto.html')

def informacion(request):
	return render(request, 'informacion.html')