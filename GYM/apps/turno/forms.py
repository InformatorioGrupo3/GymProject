from django import forms
from django.forms import ModelForm
from GYM.apps.registro.models import *
from .models import turno

class registrar_turno(forms.ModelForm):
	class Meta:
		model = turno
		fields = '__all__'
	
	def __str__(self):
		return super(cliente).__str__()