from django.urls import path
from . import views

# Configuración URL de la app inicio
# Si agrego funciones en la view de la app inicio debo agregar los path acá

urlpatterns = [
    path('', views.inicio, name='index'),
   
]