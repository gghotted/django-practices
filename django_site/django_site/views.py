from django.conf import settings
from django.http.response import JsonResponse

from django_site.tasks import send_email


def test_send_email(request):
    send_email.delay('send test', '', [settings.EMAIL_HOST_USER])
    return JsonResponse({'send': True})
