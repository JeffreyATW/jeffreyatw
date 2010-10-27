from jeffreyatw.portfolio.models import Entry, Section
from django.shortcuts import render_to_response

def index(request):
    expose = {}
    expose['sections'] = []
    sections = Section.objects.all().order_by("id")
    for section in sections:
        section.entries = section.get_entries()
        expose['sections'].append(section)
    return render_to_response('portfolio/index.html', expose)
