from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django import forms


class usuario(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    dni = models.PositiveIntegerField(unique=True, blank=False, help_text='DNI sin puntos')
    password = models.CharField(null=False, max_length=30)
    email = models.EmailField(blank=True)
    telefono = models.CharField(blank=True, null=True, max_length=20)
    foto = models.ImageField(upload_to= 'foto_usuario', null=True, blank=True)
    habilitado = models.BooleanField(default=True)

    class Meta:
        db_table = 'usuarios'
        ordering = ['apellido', 'nombre']
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return f'{self.apellido}, {self.nombre} - DNI: {self.dni}'

'''
class usuario(User):
    #first_name = models.CharField(max_length=50, blank=False)
    #last_name = models.CharField(max_length=50, blank=False)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    dni = models.PositiveIntegerField(unique=True, blank=False, help_text='DNI sin puntos')
    #password = models.CharField(null=False, max_length=30)
    #email = models.EmailField(blank=True)
    telefono = models.CharField(blank=True, null=True, max_length=20)
    foto = models.ImageField(upload_to= 'foto_usuario', null=True, blank=True)
    habilitado = models.BooleanField(default=True)

    class Meta:
        db_table = 'usuarios'
        ordering = ['last_name', 'first_name']
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return f'{self.apellido}, {self.nombre} - DNI: {self.dni}'
'''