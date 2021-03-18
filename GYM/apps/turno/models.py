from django.db import models
from django.db.models import F, Count
from apps.registro.models import *


class actividad(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False, unique=True)
    nombre_corto = models.CharField(max_length=3, null=False, blank=False, unique=True)
    cupo_max = models.PositiveSmallIntegerField(
        verbose_name='Cupo máximo de personas',
        blank=False,
        null=False,
    )
    descripcion = models.TextField(blank=True, max_length=200, default='')
    disponible = models.BooleanField(default=True)

    class Meta:
        db_table = 'actividades'
        ordering = ['nombre', 'cupo_max']
        verbose_name = 'actividad'
        verbose_name_plural = 'actividades'

    def __str__(self):
        return self.nombre


class turno(models.Model):
    usuario = models.ManyToManyField(
        usuario,
        verbose_name='usuarios en este turno',
        name='usuario',
        blank=True,
        limit_choices_to={
            'is_active': True,
            'is_staff': False,
        }
    )

    actividad = models.ForeignKey(
        actividad,
        on_delete=models.CASCADE,
        name='actividad',
        limit_choices_to={'disponible':True},
    )

    fecha = models.DateField()
    horario = models.TimeField()
    disponible = models.BooleanField(default=True)
    #cupo_actual = models.SmallIntegerField(default=0, editable=False)
    #cupo_max = models.SmallIntegerField(editable=False, default=37)

    @property
    def cupo_actual(self):
        cupo = turno.usuario.through.objects.filter(turno__id=self.id).count()
        return cupo

    @property
    def cupo_max(self):
        limite = self.actividad.cupo_max
        resultado = self.cupo_actual < limite
        self.disponible = resultado
        return limite

    @property
    def actualizacion(self):
        resultado = self.cupo_actual < self.cupo_max
        self.disponible = resultado
        return resultado

    @property
    def nombre(self):
        texto = f'{self.actividad.nombre_corto}_'
        for i in str(self.fecha).split('-'):
            texto += ''.join(i)
        texto += '_'
        for i in str(self.horario).split(':')[:2]:
            texto += ''.join(i)
        return texto

    class Meta:
        db_table = 'turnos'
        ordering = ['actividad', 'horario']
        verbose_name = 'turno'
        verbose_name_plural = 'turnos'
        unique_together = ('actividad', 'horario', 'fecha')

    def __str__(self):
        return self.nombre