from django.shortcuts import render_to_response
from jeffreyatw.portfolio.models import Section

def index(request):
    expose = {}
    expose['sections'] = Section.objects.exclude(name='Contact')
    return render_to_response('landing/index.html', expose)
