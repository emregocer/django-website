from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='bz2iwqqxj0)k1g!befzf*#b&50nt_lnv#n7vl@%#ly_o^er^85')

DEBUG = env.bool('DJANGO_DEBUG', default=True)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(ROOT_DIR.path('db.sqlite3')),
    }
}

FIXTURE_DIRS = (
    str(CONFIG_DIR.path('fixtures')),
)