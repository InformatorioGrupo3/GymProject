from django.db import models
from apps.registro.models import *

class actividad(models.Model):   
    nombre = models.CharField(max_length=50, null=False, blank=False, unique=True)
    cupo_max = models.PositiveSmallIntegerField(
        verbose_name='Cupo máximo de personas',
        blank=False,
        null=False
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
    cliente = models.ManyToManyField(
        cliente,
        verbose_name='clientes en este turno',
        name='cliente',
        blank=True,
        limit_choices_to={'is_active':True},
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

    '''
    def ingresar_usuario(self, usuario, turno):
        resultado = False
        if turno.actividad.cupo_max < turno.cupo_actual:
            pass
        else:
            turno.cupo_actual += 1
            resultado = True
            turno.save()
        
        return resultado
    '''
    def __str__(self):
        return f'{str(self.id).zfill(5)} {self.actividad} / {self.horario}'