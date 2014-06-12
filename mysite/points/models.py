from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class Point(models.Model):
    summoner_name = models.CharField(max_length=120)

    def __unicode__(self):
        return smart_unicode(self.summoner_name)