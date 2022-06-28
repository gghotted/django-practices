from .base import *

DEBUG = DEPLOY_SECRET['DEBUG']

ALLOWED_HOSTS = DEPLOY_SECRET['ALLOWED_HOSTS']

WSGI_APPLICATION = 'django_site.wsgi.deploy.application'

DATABASES = {'default': DEPLOY_SECRET['DATABASES']}

CELERY_BROKER_URL = 'redis://%s:6379/0' % DEPLOY_SECRET['CELERY_BROKER_URL']
CELERY_RESULT_BACKEND = 'redis://%s:6379/0' % DEPLOY_SECRET['CELERY_RESULT_BACKEND']
