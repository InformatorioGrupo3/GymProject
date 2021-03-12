from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_gym_patito.sqlite3'),
    }
}

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_gym_patito', # --> NOMBRE DE LA BASE YA CREADA
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '',     # Vacío = localhost
        'PORT': '3306',
    }
}