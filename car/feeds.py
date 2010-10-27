from django.contrib.syndication.feeds import Feed
from jeffreyatw.car.models import Comic

class LatestComics(Feed):
    title = "CAR"
    link = "/car/"
    description = "CAR comic updates."
    
    def items(self):
        return Comic.objects.order_by('-pub_date')[:5]
