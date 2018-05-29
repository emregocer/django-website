from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bz2iwqqxj0)k1g!befzf*#b&50nt_lnv#n7vl@%#ly_o^er^85'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_app_db',
        'USER': 'django_app_user',
        'PASSWORD': 'django_db_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}