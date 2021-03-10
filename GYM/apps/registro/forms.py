
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class registrar_cliente(UserCreationForm):
    class Meta:
        model = cliente
        fields = ('username', 'email')

class editar_cliente(UserChangeForm):
    class Meta:
        model = cliente
        fields = ('username', 'email')

'''
class registrar_cliente(forms.ModelForm):
	class Meta:
		model = cliente
		widgets = {
        'password': forms.PasswordInput(),
    }
		fields = '__all__'
	
	def __str__(self):
		return super(cliente).__str__()

'''		

'''
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *

class registrar_cliente(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = cliente
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            #'password2',
        )
'''