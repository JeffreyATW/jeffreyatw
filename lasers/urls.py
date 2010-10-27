from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': \
     'lasers/index.html'}),
    (r'^coords', 'jeffreyatw.lasers.views.coords'),
)
