import os

from celery import Celery
from django.core.mail import EmailMessage

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task
def send_email(subject, body, to):
    message = EmailMessage(subject, body, to=to)
    message.send()
