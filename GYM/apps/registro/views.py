from django.shortcuts import render, redirect
from .forms import registrar_cliente

def registro(request):
	if request.method == 'POST':
		form = registrar_cliente(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index')
	else:
		form = registrar_cliente()
	return render(request, 'registro.html', {'form': form})