from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
      model = Player
    summoner_name = forms.CharField(max_length=20)
    kills = forms.IntegerField(required=False) #approves of no input
