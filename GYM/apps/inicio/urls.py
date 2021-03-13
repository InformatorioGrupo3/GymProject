from django.urls import path
from .views import *
from django.views.generic.base import TemplateView

# Configuración URL de la app inicio
# Si agrego funciones en la view de la app inicio debo agregar los path acá

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    #path('contacto/', TemplateView.as_view(), name='contacto'),
    #path('informacion/', TemplateView.as_view(), name='informacion'),
    #path('perfil/', TemplateView.as_view(), name='perfil'),
    

]
    '''
    path('', views.inicio, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('informacion/', views.informacion, name='informacion'),
    path('perfil/', views.perfil, name='perfil'),
    '''