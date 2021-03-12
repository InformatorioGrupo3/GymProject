from django import forms
from .models import usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registrar_cliente(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
	
	def __str__(self):
		return super(usuario).__str__()

