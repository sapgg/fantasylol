from django.contrib import admin

# Register your models here.
from .models import Player

class PlayerAdmin(admin.ModelAdmin):
    class Meta:
        model = Player

admin.site.register(Player, PlayerAdmin)
