from django.urls import path
from . import views

# Configuración URL de la app login
# Si agrego funciones en la view de la app login debo agregar los path acá

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
   
]