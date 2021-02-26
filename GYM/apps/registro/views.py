from django.shortcuts import render, redirect
from .forms import registrarCliente


# Create your views here.
def registro(request):
	if request.method == 'POST':
		form = registrarCliente(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index')
	else:
		form = registrarCliente()
	return render(request, 'registro.html', {'form': form})
