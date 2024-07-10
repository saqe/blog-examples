from .base import *
import os


SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEBUG = False
ALLOWED_HOSTS = ["domain.com"]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        # ...
        "OPTIONS": {
            # ...
        },
    },
}