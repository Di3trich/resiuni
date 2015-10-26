from django.conf.urls import patterns, include, url

from views import *

urlpatterns = patterns('',
    url(r'^$', show_main),
    url(r'^test/$', show_residencias),
)
