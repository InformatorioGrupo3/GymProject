from django.urls import path
from .views import *

# Configuración URL de la app registro
# Si agrego funciones en la view de la app registro debo agregar los path acá
urlpatterns = [
    path('', registrar_cliente_vista.as_view(), name='registro'),
]