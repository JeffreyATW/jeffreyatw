import datetime
from django.conf.urls.defaults import *
from django.conf import settings
from jeffreyatw.car.models import Comic, Character
from jeffreyatw.car.feeds import LatestComics

today = datetime.date.today().isoformat()
all = Comic.objects.order_by('-pub_date')
latest_date = all.filter(pub_date__lte=today)[0].pub_date.isoformat()

info_dict = {
    'queryset': Character.objects.all(),
}

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^characters/{0,1}$', 'django.views.generic.list_detail.object_list', \
     info_dict),
    (r'^characters/(?P<object_id>\d+)/{0,1}$', \
     'django.views.generic.list_detail.object_detail', info_dict),
    (r'^archive/{0,1}$', 'django.views.generic.list_detail.object_list', \
     {'queryset': all}),
    (r'^(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})/play/{0,1}$', \
     'jeffreyatw.car.views.detail', {'play': True}),
    (r'^(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})/{0,1}$', \
     'jeffreyatw.car.views.detail'),
    (r'^play/{0,1}$', 'jeffreyatw.car.views.detail', {'date':latest_date, \
     'play': True, 'links':True}),
    (r'^$', 'jeffreyatw.car.views.detail', {'date':latest_date, 'links': \
                                            True}),
    (r'^js/calendar.js$', 'jeffreyatw.car.views.music'),
    (r'^rss.*', 'django.contrib.syndication.views.feed', {'feed_dict': \
     {'latest':LatestComics}, 'url':'latest'}),
    (r'^media/(?P<path>.*)$', 'django.views.generic.simple.redirect_to', \
     {'url': '/static/car/media/%(path)s'}),
    (r'^panels/(?P<path>.*)$', 'django.views.generic.simple.redirect_to', \
     {'url': '/static/car/media/panels/%(path)s'}),
    (r'^car(?P<path>[^\/]*\.(png|gif|jpg)$)', 'django.views.generic.simple.redirect_to', {'url' : '/static/car/media/panels/car%(path)s'}),
    (r'(?P<path>[^\/]*\.(png|gif|jpg)$)', 'django.views.generic.simple.redirect_to', {'url' : '/static/car/%(path)s'}),
)
