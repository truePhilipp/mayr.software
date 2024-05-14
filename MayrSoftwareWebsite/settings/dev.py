from .base import *


SECRET_KEY = 'django-insecure-b8vyrkhkg8qhzejf++hj1a%l&0#3kut=$e5pd8y8$d0@imy+-0'
DEBUG = True
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}