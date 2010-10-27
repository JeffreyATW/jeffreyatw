from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'jeffreyatw.binaryimage.views.index',),
    (r'^ascii$', 'jeffreyatw.binaryimage.views.ascii',),
    (r'^binary$', 'jeffreyatw.binaryimage.views.binary',),
)
