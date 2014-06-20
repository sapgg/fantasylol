from django.db import models
from django.utils.encoding import smart_unicode
from django import forms

# Create your models here.

class Player(models.Model):
    summoner_name = models.CharField(max_length=120)
    kills = models.IntegerField(null=True, blank=True) #makes the field able to accept no input

    def __unicode__(self):
        return smart_unicode(self.summoner_name)