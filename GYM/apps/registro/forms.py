from django import forms
# from .models import Cliente 

class registrarCliente(forms.ModelForm):
	class Meta:
#		model = Cliente
		fields = '__all__'
