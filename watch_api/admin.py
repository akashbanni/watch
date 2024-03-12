from django.contrib import admin
from .models import watch_movie,watch_platform

# Register your models here.
admin.site.register(watch_movie)
admin.site.register(watch_platform)
