from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
      model = Player
    summoner_name = forms.CharField(max_length=20)
