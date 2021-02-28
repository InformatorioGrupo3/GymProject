from django.urls import path
from . import views

# Configuración URL de la app registro
# Si agrego funciones en la view de la app registro debo agregar los path acá
urlpatterns = [
    path('', views.registro_usuario.as_view(), name='registro'),
]