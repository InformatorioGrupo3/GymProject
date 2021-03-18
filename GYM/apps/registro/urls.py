from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', registrar_usuario_vista.as_view(), name='registro'),
    path('editar/<int:pk>/', editar_usuario_vista.as_view(), name='editar'),
]