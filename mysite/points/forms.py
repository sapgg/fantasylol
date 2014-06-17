from django import forms
from .models import Point

class PointForm(forms.Form):
    #class Meta:
    #  model = Point
    summoner_name = forms.CharField(max_length=20)
