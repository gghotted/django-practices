from .base import *

DEBUG = DEBUG_SECRET['DEBUG']

ALLOWED_HOSTS = DEBUG_SECRET['ALLOWED_HOSTS']

WSGI_APPLICATION = 'django_site.wsgi.debug.application'
