from django.db import models


# class actividades(models.Model):
#     Zumba = 'Zumba'
#     Funcional = 'Funcional'
#     Aerobic = 'Aerobic'
#     Musculacion = 'Musculacion'
#     Spinning = 'Spinning'
#     actividades_gym = [
#         (None, 'Seleccione una opcion'),
#         (Zumba, 'Zumba'),
#         (Funcional, 'Funcional'),
#         (Aerobic, 'Aerobic'),
#         (Musculacion, 'Musculacion'),
#         (Spinning, 'Spinning'),
#     ]
#     actividad = models.CharField(
#         max_length = 12,
#         choices = actividades_gym,
#         default = None,
#     )


# class turno(models.Model, usuario, actividades):
#     usuario = models.ManyToManyField(usuario, on_delete=models.CASCADE)
#     actividad = models.ForeignKey(actividades, on_delete=models.CASCADE)
#     cupo = models.CharField(max_length=50)
#     horario = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return super.usuario, 'Actividad: {}\n Horario:{}'.format(self.actividad, self.horario)
