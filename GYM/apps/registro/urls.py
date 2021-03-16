from django.urls import path
from .views import *


urlpatterns = [
    path('registrar_usuario/', registrar_usuario_vista.as_view(), name='registro'),
]