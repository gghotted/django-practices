from django.shortcuts import render
from django.utils.translation import gettext as _


def test_view(request):
    context = {
        'context': _('context'),
    }
    return render(request, 'post/test.html', context)
