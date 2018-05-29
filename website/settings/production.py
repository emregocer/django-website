import os
from .base import *

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'django_db_user',
        'PASSWORD': os.environ.get('DATABASE_USER_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}