"""django_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from post import views

'''
path not found시 언어를 추가하여 redirect함
ex) /admin/ : if not found -> /ko/admin/
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test', views.test_view),
]

'''
prefix_default_language == False : 기본 로케일을 settings.LANGUAGE_CODE로
prefix_default_language == True : 기본 로케일을 request의 실제 로케일로?
'''
urlpatterns += i18n_patterns(*urlpatterns, prefix_default_language=False)
