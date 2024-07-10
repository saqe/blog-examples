import os

from .base import *


SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-s%!v_0#(pwvjz1@uj(co939nzm*9%bhqe4xzcvd2ybhj3)2hl3')

DEBUG = True
ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
