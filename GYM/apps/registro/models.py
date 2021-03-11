from django.db import models
from django.contrib.auth.models import AbstractUser

class usuario(AbstractUser):
    fecha_nacimiento = models.DateField(blank=True, null=True, help_text='DD-MM-AAAA')
    dni = models.PositiveIntegerField(unique=True, blank=False, help_text='DNI sin puntos', null=True)
    telefono = models.CharField(blank=True, default='', max_length=20)
    foto = models.ImageField(upload_to='foto_usuario', null=True, blank=True)

    class Meta:
        db_table = 'usuarios'
        ordering = ('last_name', 'first_name',)
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return self.username
