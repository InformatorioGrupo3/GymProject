from django.urls import path
from . import views

# Configuración URL de la app registro
# Si agrego funciones en la view de la app registro debo agregar los path acá
urlpatterns = [
    path('', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
   
]