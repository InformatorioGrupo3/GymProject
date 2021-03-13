from GYM.settings.base import *
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
"""
MODIFICACIONES PARA EL USO DE DESARROLLO
"""
# Aquí van las apps que voy creando 

MIS_APPS = [
    'apps.inicio',
    'apps.registro',
    'apps.login',
    'apps.turno',
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

'''
# Para encriptar contraseñas de usuarios
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'accounts.hashers.PBKDF2WrappedSHA1PasswordHasher',
]
'''
# Elegir la DB para usar en local
# DATABASES = db.MYSQL
DATABASES = db.SQLITE

# En caso de que localmente utilice un horario distinto al base
LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Buenos_Aires'


STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), 'static'),
    )

MEDIA_URL = '/media/'
MEDIA_ROOT= os.path.join(os.path.dirname(BASE_DIR), 'media')

AUTH_USER_MODEL = 'registro.usuario'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'