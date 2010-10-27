from jeffreyatw.portfolio.models import Entry, Section
from jeffreyatw.portfolio.forms import EntryForm
from django.contrib import admin

class EntryAdmin(admin.ModelAdmin):
    model = Entry
    form = EntryForm

admin.site.register(Entry, EntryAdmin)
admin.site.register(Section)
