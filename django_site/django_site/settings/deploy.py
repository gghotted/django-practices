from .base import *

DEBUG = DEPLOY_SECRET['DEBUG']

ALLOWED_HOSTS = DEPLOY_SECRET['ALLOWED_HOSTS']

WSGI_APPLICATION = 'django_site.wsgi.deploy.application'

DATABASES = {'default': DEPLOY_SECRET['DATABASES']}
