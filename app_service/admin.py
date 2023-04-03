from django.contrib import admin

from .models import *


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'protocol', 'domain', 'domain_zone', 'path']
