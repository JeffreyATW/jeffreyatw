import datetime, re, urlparse
from django.core.exceptions import PermissionDenied
from django.utils import simplejson
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from jeffreyatw.car.forms import CommentForm, CaptchaForm
from jeffreyatw.car.models import Comic, Comment

today = datetime.date.today().isoformat()

def referer_matches_hostname(*netlocs):
    """
    Decorator for views that checks that if the request's HTTP_REFERER matches
    the supplied string. Failure raises a PermissionDenied exception. If
    multiple arguments are supplied the decorator will try to match any of
    them.
    """
    def _dec(view_func):
        def _check_referer(request, *args, **kwargs):
            referer = request.META.get('HTTP_REFERER', '').replace("www.", "")
            referer_netloc = urlparse.urlparse(referer).netloc
            if referer_netloc in netlocs:
                return view_func(request, *args, **kwargs)
            raise PermissionDenied()
        _check_referer.__doc__ = view_func.__doc__
        _check_referer.__dict__ = view_func.__dict__        
        return _check_referer
    return _dec

from django.contrib.sites.models import Site
local_referer_only = referer_matches_hostname(str(Site.objects.get_current()))

local_referer_only.__doc__ = (
    """
    Decorator for views that checks that if the request's HTTP_REFERER matches
    the current site. If not, a PermissionDenied exception is raised.
    """
)

def detail(request, date, play=False, links=False):
    if request.method == "POST":
        valid = False
        fc = CaptchaForm(request.POST, initial={'captcha': \
                                                request.META['REMOTE_ADDR']})
        if fc.is_valid():
            c = Comic.objects.get(pub_date=date)
            f = CommentForm(request.POST)
            try:
                d = f.save(commit=False)
                d.comic = c
                d.ip = request.META['REMOTE_ADDR']
                d.save()
                # Always return an HttpResponseRedirect after successfully
                # dealing with POST data. This prevents data from being posted
                # twice if a user hits the Back button.
                response_dict = {}
                response_dict.update({'name': d.name, 'website': d.website, \
                                      'content': d.content, 'pub_date': \
                                      d.pub_date.strftime( \
                                      "%B %e, %Y %I:%M %p")})
                valid = True
            except ValueError:
                pass
        if valid == False:
            response_dict = {}
            response_dict.update({'error':
                                  '<p style="color: red; font-weight: bold"> \
                                   There was an error with your comment. \
                                   Please check it and try again.</p>'})
        return HttpResponse(simplejson.dumps(response_dict), \
                            mimetype='application/javascript')
    try:
        c = Comic.objects.get(pub_date=date)
    except Comic.DoesNotExist:
        raise Http404
    # dates
    dates_set = Comic.objects.order_by('-pub_date').filter(pub_date__lte=today)
    dates_list = []
    for i in dates_set:
        dates_list.append(i.pub_date.strftime('%Y%m%d'))
    dates = ",\n".join(dates_list)
    # range
    first_year = Comic.objects.order_by('pub_date')[0].pub_date.strftime('%Y')
    latest_year = c.pub_date.strftime('%Y')
    year_range = "%s,%s" % (first_year, latest_year)
    # form
    f = CommentForm()
    f.fields['content'].label = "Comments (plain text only)"
    fc = CaptchaForm()
    return render_to_response('car/comics/comic_detail.html', {'object':c, \
                              'play':play, 'links':links, 'dates':dates, \
                              'range':year_range, 'form':f, 'captcha':fc})
    
@local_referer_only
def music(request):
    referer = request.META.get('HTTP_REFERER', '')
    referer_path = urlparse.urlparse(referer).path
    try:
        date = re.search('[0-9]{4}-[0-9]{2}-[0-9]{2}', referer_path).group(0)
        c = Comic.objects.get(pub_date=date)
    except AttributeError:
        c = Comic.objects.order_by('-pub_date').filter(pub_date__lte=today)[0]
    return render_to_response('car/comics/music.html', {'object': c})
