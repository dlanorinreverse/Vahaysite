# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
from .models import Vahay, Review, Image, WorldBorder


class vahayAdmin(LeafletGeoAdmin):
	pass


admin.site.register(Vahay, vahayAdmin)
admin.site.register(Review)
admin.site.register(Image)
admin.site.register(WorldBorder, admin.GeoModelAdmin)