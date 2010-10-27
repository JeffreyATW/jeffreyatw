from datetime import date
from django.db import models
from jeffreyatw.portfolio import storage

overwrite = storage.OverwriteStorage()

class Entry(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    image = models.ImageField(upload_to="portfolio/2009", blank=True, \
                              storage=overwrite)
    thumb1 = models.ImageField(upload_to="portfolio/2009", blank=True, \
                               storage=overwrite)
    thumb2 = models.ImageField(upload_to="portfolio/2009", blank=True, \
                               storage=overwrite)
    thumb3 = models.ImageField(upload_to="portfolio/2009", blank=True, \
                               storage=overwrite)
    description = models.TextField()
    pub_date = models.DateField(default=date.today().strftime('%Y-%m-%d'))
    section = models.ForeignKey('Section')

    def __unicode__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
    
    def get_entries(self):
        return Entry.objects.filter(section=self).order_by("-pub_date")
