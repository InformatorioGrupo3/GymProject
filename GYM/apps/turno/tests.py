from django.test import TestCase
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GYM.settings.local')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from .models import usuario

# Select * From table
var = usuario.objects.all()
print(var)

# Insercion 
var = usuario()
var.nombre = 'NombreX'
usuario.save()

# Edicion
var = usuario.objects.get(id=1)
print(var.nombre) # Me muestra el nombre de dicho id

# Eliminacion
var = usuario.objects.get(id=1)
var.delete
