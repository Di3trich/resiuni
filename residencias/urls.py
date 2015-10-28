from django.conf.urls import patterns, include, url

from views import *

urlpatterns = patterns('',
    url(r'^$', show_main),
    url(r'^test/$', show_residencias),
    url(r'^test2/$', test),
    url(r'^form/search/$', super_function_show),
)
