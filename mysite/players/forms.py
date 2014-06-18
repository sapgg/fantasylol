from django import forms
from .models import Player

class PlayerForm(forms.Form):
    #class Meta:
    #  model = Point
    summoner_name = forms.CharField(max_length=20)
