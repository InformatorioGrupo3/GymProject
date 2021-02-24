from .base import *

"""
MODIFICACIONES PARA EL USO DE DESARROLLO
"""
import os

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent 

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

# Aquí van las apps que voy creando 

MIS_APPS = [
    'apps.inicio',
    'apps.registro',
    'apps.login',
]

INSTALLED_APPS = DJANGO_APPS + MIS_APPS




TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(BASE_DIR), 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Configuración de MySQL
'''
 DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_gym_patito', --> NOMBRE DE LA BASE YA CREADA
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',     # Vacío = localhost
        'PORT': '3306',
     }
 }
'''


LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Buenos_Aires'


STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), 'static'),
    )

MEDIA_URL = '/media/'
MEDIA_ROOT= os.path.join(os.path.dirname(BASE_DIR), 'media')