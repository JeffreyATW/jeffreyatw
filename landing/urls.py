from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'jeffreyatw.landing.views.index',),
)
