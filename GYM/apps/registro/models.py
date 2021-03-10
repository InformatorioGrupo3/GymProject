from django.db import models
import datetime
from django.contrib.auth.models import User, AbstractUser

'''
class usuario(models.Model):
    apellido = models.CharField(max_length=50, blank=False)
    nombre = models.CharField(max_length=50, blank=False)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    dni = models.PositiveIntegerField(unique=True, blank=False, help_text='DNI sin puntos', null=False)
    password = models.CharField(null=False, max_length=30)
    email = models.EmailField(blank=True)
    telefono = models.CharField(blank=True, null=True, max_length=20)
    foto = models.ImageField(upload_to= 'foto_usuario', null=True, blank=True)
    habilitado = models.BooleanField(default=True)
    fecha_ingreso = models.DateTimeField(editable=False, default=datetime.datetime.now, null=True)

    class Meta:
        db_table = 'usuarios'
        ordering = ['apellido', 'nombre']
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return f'{self.apellido}, {self.nombre} - DNI: {self.dni}'
'''

class cliente(AbstractUser):
    #usuario = models.OneToOneField(User, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    dni = models.PositiveIntegerField(unique=True, blank=False, help_text='DNI sin puntos', null=True)
    telefono = models.CharField(blank=True, null=True, max_length=20)
    foto = models.ImageField(upload_to= 'foto_usuario', null=True, blank=True)

    '''
    class Meta:
        db_table = 'clientes'
        ordering = ('last_name', 'first_name',)
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
    '''

    def __str__(self):
        return self.username
