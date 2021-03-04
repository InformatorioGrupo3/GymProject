from django.urls import path
from . import views
from django.contrib.auth import login, logout
from apps.login.views import login_form, logout_user
# Configuración URL de la app login
# Si agrego funciones en la view de la app login debo agregar los path acá

urlpatterns = [
    path('', login_form.as_view(), name='login'),
    path('logout/', views.logout_user.as_view(), name='logout'), # CORREGIR LOGOUT
    # path('logout/', views.logout, name='logout'),
    
]