from django.contrib import admin

# Register your models here.
from .models import Point

class PointAdmin(admin.ModelAdmin):
    class Meta:
        model = Point

admin.site.register(Point, PointAdmin)
