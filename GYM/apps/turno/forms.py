from django import forms
from django.forms import ModelForm
from apps.registro.models import *
from .models import *

class registrar_turno(forms.ModelForm):
	class Meta:
		model = turno
		fields = '__all__'


class ver_turno(forms.ModelForm):
	class Meta:
		model = turno
		fields = '__all__'