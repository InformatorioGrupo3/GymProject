from django.db import models
from django.utils.timezone import now
from GYM.settings.local import MEDIA_URL, STATIC_URL
from django.contrib.auth.models import User
from django import forms


class usuario(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    dni = models.PositiveIntegerField(unique=True, blank=False, help_text='DNI sin puntos')
    password1 = models.CharField(null=False, max_length=30)
    password2 = models.CharField(null=False, max_length=30)
    email = models.EmailField(blank=True)
    telefono = models.CharField(blank=True, null=True, max_length=20)
    foto = models.ImageField(upload_to= 'foto_usuario', null=True, blank=True)
    habilitado = models.BooleanField(default=True)

    def get_img(self):
        if self.foto:
            return '{}{}'.format(MEDIA_URL, self.foto)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')



    class Meta:
        db_table = 'usuarios'
        ordering = ['apellido', 'nombre']
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return f'{self.apellido}, {self.nombre} - DNI: {self.dni}'

