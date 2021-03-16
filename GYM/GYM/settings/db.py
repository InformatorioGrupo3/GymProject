from pathlib import Path
import os
import MySQLdb


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
        'NAME': 'gympatito', 
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',     
        'PORT': '3306',
    }
}

