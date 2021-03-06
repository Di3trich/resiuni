from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^residencias/', include('residencias.urls') ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'thirdauth.views.home', name='home'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
)
