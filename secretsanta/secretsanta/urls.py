"""secretsanta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls import patterns

from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # user auths urls
    url(r'^accounts/login/$', 'secretsanta.views.login'),
    url(r'^accounts/auth/$', 'secretsanta.views.auth_view'),
    url(r'^accounts/logout/$', 'secretsanta.views.logout'),
    url(r'^accounts/loggedin/$', 'secretsanta.views.loggedin'),
    url(r'^accounts/invalid/$', 'secretsanta.views.invalid_login'),
    url(r'^accounts/register/$', 'secretsanta.views.register_user'),
    url(r'^accounts/register_success/$', 'secretsanta.views.register_success'),

    url(r'', include('secretsantaapp.urls'))
]
