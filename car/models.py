import random
import time
from datetime import date, datetime
from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=200)
    image_name = models.CharField(max_length=200)
    photo_name = models.CharField(max_length=200)
    content = models.TextField()
    current = models.IntegerField(max_length=1)
    def __unicode__(self):
        return self.name
    def first_appearance(self):
        return self.all_appearances()[0]
    def all_appearances(self):
        today = date.today().isoformat()
        return Comic.objects.order_by('pub_date').filter( \
               pub_date__lte=today).filter(characters__pk=self.pk)

class Comic(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    content = models.TextField()
    episode = models.IntegerField(max_length=11)
    panels = models.IntegerField(max_length=11, default=4)
    music = models.CharField(max_length=200)
    music_title = models.CharField(max_length=200)
    characters = models.ManyToManyField(Character)
    def __unicode__(self):
        if self.episode:
            return "CAR #%d: %s" % (self.episode, self.title)
        else:
            return "CAR #%s" % self.title
    def get_absolute_url(self):
        return "http://www.jeffreyatw.com/car/%s" % (self.pub_date)
    def is_future(self):
        return self.pub_date.date() > datetime.date.today()
    ordering = ['episode']
    def get_previous_entry(self):
        return self.get_previous_by_pub_date()
    def get_next_entry(self):
        return self.get_next_by_pub_date()
    def get_comments(self):
        return Comment.objects.filter(comic=self)
    def fake_nickname(self):
        nick_1 = ["Cool", "Uber", "Mega", "Crazy", "Geek", "Awesome", \
                  "Kawaii", "Mecha", "Instant", "Weird", "Horrible", \
                  "Mario", "Sonic", ""]
        nick_2 = ["", " "]
        nick_3 = ["Dude", "Gal", "Zilla", "Neko", "Loser", "Head", "Mom", \
                  "Chick", "Guy", ""]
        nick_4 = ["69", "231", "42", "ATW", "X", "Omega", "9000", ""]
        nickname = "%s%s%s%s%s" % (nick_1[random.randrange(len(nick_1))], \
                                   nick_2[random.randrange(len(nick_2))], \
                                   nick_3[random.randrange(len(nick_3))], \
                                   nick_2[random.randrange(len(nick_2))], \
                                   nick_4[random.randrange(len(nick_4))])
        if not random.randrange(2):
            nickname = nickname.lower()
        elif not random.randrange(5):
            nickname = nickname.upper()
        return nickname
    def fake_content(self):
        exclamations = ["LOL!!!", "Haha", "", "OMG,", "LOL!", "lol", "Wow,"]
        adjectives = ["priceless", "awesome", "perfect", "so well drawn", \
                      "really unique", "so expressive", "BEST", \
                      "teh uber smex", "awfully funny", "soooo good", \
                      "major lols", "really convincing"]
        content = "%s %s's expression in panel %d is %s%s" % \
                  (exclamations[random.randrange(len(exclamations))], \
                  self.characters.all()[random.randrange(len( \
                  self.characters.all()))], random.randint(1, self.panels), \
                  adjectives[random.randrange(len(adjectives))], "!" * \
                  random.randint(1, 5))
        if not random.randrange(3):
            content = content.lower()
        elif not random.randrange(10):
            content = content.upper()
        return content
    def fake_date(self):
        stime = time.mktime(self.pub_date.timetuple())
        try:
            etime = time.mktime(self.get_next_entry().pub_date.timetuple())
        except Comic.DoesNotExist:
            etime = time.mktime(datetime.now().timetuple())
        ptime = stime + random.random() * (etime - stime)
        comment_date = time.strftime("%B %e, %Y %I:%M %p", \
                       time.localtime(ptime))
        return comment_date

class Comment(models.Model):
    name = models.CharField(max_length=200)
    website = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    comic = models.ForeignKey("Comic")
    enabled = models.IntegerField(max_length=1, default=1)
    ip = models.IPAddressField()
    def __unicode__(self):
        return self.content
