# from .base import *
from . import *  # noqa
# SECURITY WARNING: don't run with debug turned on in production!
import os

from .__init__ import *
SECRET_KEY =os.getenv("DJANGO_SECRET_KEY")


DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST",'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


CSRF_TRUSTED_ORIGINS = [ "https://harmony.shubpy.com","http://localhost:8000","http://harmony.shubpy.com"]
CORS_ALLOW_ALL_ORIGINS = True


