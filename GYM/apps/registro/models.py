from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django import forms

class usuario(models.Model):
    nombre = models.TextField(max_length=50, blank=False)
    apellido = models.TextField(max_length=20, blank=False)
    edad = models.PositiveIntegerField()
    dni = models.CharField(max_length=9, unique=True, blank=False)
    contraseña = models.CharField(null=False, max_length= 20)
    email = models.EmailField(blank=True)
    telefono = models.IntegerField(blank=True, null=True)
    foto = models.ImageField(upload_to= 'foto_usuario', null=True, blank=True)

    class Meta:
        db_table = 'usuarios'
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return 'Usuario {}, {} \n DNI: {}'.format(self.apellido, self.nombre, self.dni)