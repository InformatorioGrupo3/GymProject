from django import forms
from django.forms import ModelForm
from apps.registro.models import usuario
from .models import turno

class registrar_turno(forms.ModelForm):
	class Meta:
		model = turno
		fields = '__all__'
	
	def __str__(self):
		return super(usuario).__str__()