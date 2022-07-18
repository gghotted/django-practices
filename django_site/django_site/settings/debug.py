from .base import *

DEBUG = DEBUG_SECRET['DEBUG']

ALLOWED_HOSTS = DEBUG_SECRET['ALLOWED_HOSTS']

WSGI_APPLICATION = 'django_site.wsgi.debug.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('127.0.0.1', 6379)],
        }
    }
}
