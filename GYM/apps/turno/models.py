from django.db import models
from apps.registro.models import usuario

class actividad(models.Model):   
    nombre = models.CharField(max_length=50, null=False, blank=False, unique=True)
    cupo_max = models.PositiveSmallIntegerField(
        verbose_name='Cupo máximo de personas',
        blank=False,
        null=False
        )
    descripcion = models.TextField(blank=True, max_length=200, default='x')
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
        limit_choices_to={'habilitado':True},
        )
    actividad = models.ForeignKey(
        actividad,
        on_delete=models.CASCADE,
        name='actividad',
        limit_choices_to={'disponible':True},
        )
    cupo_actual = models.PositiveSmallIntegerField(default=0)
    horario = models.DateTimeField()
    disponible = models.BooleanField(default=True)

    class Meta:
        db_table = 'turnos'
        ordering = ['actividad', 'horario']
        verbose_name = 'turno'
        verbose_name_plural = 'turnos'
        unique_together = ('actividad', 'horario')

    def __str__(self):
        return f'{str(self.id).zfill(5)} {self.actividad} / {self.horario}'