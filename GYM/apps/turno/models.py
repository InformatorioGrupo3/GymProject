from django.db import models
from apps.registro.models import usuario

class actividades(models.Model):   
    nombre = models.CharField(max_length=50, null=False, blank=False, unique=True)
    cupo_max = models.PositiveSmallIntegerField(
        verbose_name='Cupo máximo de personas',
        blank=False,
        null=False
        )

#Lo que está comentado no sirve, se agregan actividades desde el admin
'''
    Zumba = 'Zumba'
    Funcional = 'Funcional'
    Aerobic = 'Aerobic'
    Musculacion = 'Musculacion'
    Spinning = 'Spinning'
    actividades_gym = [
        (None, 'Seleccione una opcion'),
        (Zumba, 'Zumba'),
        (Funcional, 'Funcional'),
        (Aerobic, 'Aerobic'),
        (Musculacion, 'Musculacion'),
        (Spinning, 'Spinning'),
    ]
    actividad = models.CharField(
        max_length = 12,
        choices = actividades_gym,
        default = None,
    )
'''

class turno(models.Model):
    usuario = models.ManyToManyField(usuario, verbose_name='usuarios en este turno', name='usuario')
    actividad = models.ForeignKey(actividades, on_delete=models.CASCADE, name='actividad')
    #cupo_max = actividades.cupo_max
    cupo_actual = models.PositiveSmallIntegerField(default=0)
    horario = models.DateTimeField(auto_now=True)
    disponible = models.BooleanField(default=True)

    class Meta:
        db_table = 'turnos'
        ordering = ['actividad', 'horario']

    def __str__(self):
        return super.usuario, 'Actividad: {}\n Horario:{}'.format(self.actividad, self.horario)

