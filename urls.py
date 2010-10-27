from django.conf import settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

rawurls = [
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^favicon.ico$', 'django.views.generic.simple.redirect_to', {'url': \
     '/static/favicon.ico'}),
    (r'^admin/{0,1}(.*)', admin.site.root),
    (r'^resume', 'django.views.generic.simple.redirect_to', {'url': \
     'http://docs.google.com/View?id=dfjgtf36_23ckhfhths&hgd=1'}), 
    (r'^atom.xml$', 'django.views.generic.simple.redirect_to', {'url': \
     '/car/rss.xml'}),
    (r'^characters.shtml$', 'django.views.generic.simple.redirect_to', \
     {'url': '/car/characters'}),
    (r'^car/', include('jeffreyatw.car.urls')),
    (r'^lasers/',  include('jeffreyatw.lasers.urls')),
    (r'^portfolio/', include('jeffreyatw.portfolio.urls')),
    (r'^binaryimage/', include('jeffreyatw.binaryimage.urls')),
    (r'^index.htm', include('jeffreyatw.landing.urls')),
    (r'^$', include('jeffreyatw.landing.urls')),
]

legacy_dirs = ['28', 'Scripts', 'bob', 'bus', 'cgi', 'comics', 'css', \
               'davegetz', 'deadwinter', 'draggy', 'drawings', 'evidence', \
               'evildavis', 'facebook', 'ff', 'food', 'gailmuldrow', 'gordon', \
               'groza', 'holocaust', 'images', 'js', 'ld', 'mario', 'media', \
               'mid', 'midgarswamp', 'movies', 'mt', 'music', 'newsidebar', \
               'pants', 'photos', 'phpMyAdmin', 'professional', 'punks', \
               'r', 'rpgcomics', 'sa', 'saddam', 'sidebar', 'sillybaby', \
               'sm', 'sophie', 'store', 'tane', 'temp', 'v10', 'v11', 'v12', \
               'v3', 'v5', 'v6', 'v7', 'v8', 'v9', 'webcam']

for legacy_dir in legacy_dirs:
    rawurls += [(r'^%s/(?P<path>.*)$' % legacy_dir, 
               'django.views.generic.simple.redirect_to', {'url': \
               '/static/%(legacy_dir)s/%(path)s', 'legacy_dir': legacy_dir})]

legacy_files = ['Library.html', 'about.gif', 'about.shtml', \
                'about_shadow.gif', 'archive.html', 'art.gif', \
                'art_shadow.gif', 'atom.xml', 'bg.jpg', 'bio.html', \
                'carbottom.html', 'carbottom_old.html', 'cartest.shtml', \
                'cartop.html', 'cartop_old.html', 'characters_old.shtml', \
                'ck_yourmom.jpg', 'comic.html', 'comics.gif', \
                'comics.shtml', 'comics_shadow.gif', 'contact.gif', \
                'contact_shadow.gif', 'ddr_sims.gif', 'ddr_sims.shtml', \
                'ddr_sims_shadow.gif', 'dropboard.swf', 'fanart.shtml', \
                'finalproject.html', 'finalproject.swf', 'foaf.rdf', \
                'footer.html', 'header.html', 'include.js', 'index.html', \
                'index.php', 'index.rdf', 'index.xml', 'index_old.shtml', \
                'index_v1.shtml', 'index_v2.shtml', 'index_v3.shtml', \
                'index_v4.shtml', 'index_v5.shtml', 'index_v6.shtml', \
                'ipod.html', 'kek.txt', 'legholestraws.txt', 'line.gif', \
                'links.shtml', 'links.shtml', 'lj_logo.fla', 'lj_logo.swf', \
                'lj_member.pdf', 'midi.shtml', 'misc.shtml', 'morlon.gif', \
                'morlon.html', 'mythoughtsexactly.txt', \
                'nav-commenters.gif', 'not_jeffrey.html', 'nutshell.txt', \
                'pants.html', 'paul.html', 'paul.swf', 'polaroid.mov', \
                'porterpamphlet.odg', 'porterpamphlet.pdf', 'saltykong.txt', \
                'slug_lj.doc', 'slug_lj.pdf', 'style.css', \
                'styles-site.css', 'styles.css', 'taka_death.html', \
                'temp.txt', 'test.html', 'thesis.pdf', 'thisisafungame.txt', \
                'too_many_eggs.jpg', 'unbendablegirder.txt', 'v5style.css', \
                'v6_blogindex.html', 'v6_bright.html', 'v6_brtop.html', \
                'v6_footer.html', 'v6_header.html', 'v6_top.html', \
                'v6style.css', 'v7_bottom.txt', 'v7_top.txt', 'webcams.gif', \
                'webcams_shadow.gif', 'whenmakefint.txt']

for legacy_file in legacy_files:
    rawurls += [(r'%s' % legacy_file, \
                 'django.views.generic.simple.redirect_to', {'url': \
                 '/static/%(legacy_file)s', 'legacy_file': legacy_file})]

urlpatterns = patterns('', *rawurls)
