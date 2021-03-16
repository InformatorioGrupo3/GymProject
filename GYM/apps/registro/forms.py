
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class registrar_usuario(UserCreationForm):
    class Meta:
        model = usuario
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'dni',
            'fecha_nacimiento',
            'telefono',
            'foto',
        )
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'dni':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento':forms.NumberInput(attrs={'type': 'date','label':'Fecha de Nacimiento','class':'form-control'}),
            'telefono':forms.TextInput(attrs={'placeholder':'3624xxxxxx','class':'form-control'}),
            'email':forms.EmailInput(attrs={'placeholder':'ejemplo@gmail.com','class': 'form-control',}),
            'password1':forms.PasswordInput(attrs={'class': 'form-control',}),
            'password2':forms.PasswordInput(attrs={'class': 'form-control',}),
        }  

class editar_usuario(UserChangeForm):
    class Meta:
        model = usuario
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'dni',
            'fecha_nacimiento',
            'telefono',
            'foto',
        )
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'dni':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento':forms.NumberInput(attrs={'type': 'date','label':'Fecha de Nacimiento','class':'form-control'}),
            'telefono':forms.TextInput(attrs={'placeholder':'3624xxxxxx','class':'form-control'}),
            'email':forms.EmailInput(attrs={'placeholder':'ejemplo@gmail.com','class': 'form-control',}),
            'password1':forms.PasswordInput(attrs={'class': 'form-control',}),
            'password2':forms.PasswordInput(attrs={'class': 'form-control',}),
        }  

