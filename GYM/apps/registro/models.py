from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django import forms

class usuario(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    dni = models.PositiveIntegerField(unique=True, blank=False, help_text='DNI sin puntos')
    contraseña = models.CharField(null=False, max_length=30)
    email = models.EmailField(blank=True)
    telefono = models.CharField(blank=True, null=True, max_length=20)
    foto = models.ImageField(upload_to= 'foto_usuario', null=True, blank=True)

    class Meta:
        db_table = 'usuarios'
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return 'Usuario {}, {} \n DNI: {}'.format(self.apellido, self.nombre, self.dni)
