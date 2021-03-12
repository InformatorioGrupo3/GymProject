from django import forms
from .models import usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registrar_cliente(UserCreationForm):
	class Meta:
		model = User
		widgets = {
        'password1' : forms.PasswordInput(),
		'password2' : forms.PasswordInput(),
    }
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
	
	def __str__(self):
		return super(usuario).__str__()