# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.

class WorldBorder(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    mpoly = models.MultiPolygonField()

    def __str__(self):             
        return self.name



class Vahay(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	rent_range = models.CharField(max_length=100)
	category = models.CharField(max_length=100)
	contact_details = models.CharField(max_length=100)
	vote = models.IntegerField(default=0)
	available = models.BooleanField(default=1)
	description = models.CharField(max_length=500, null=True)
	address = models.CharField(max_length=500, null=True)
	location = models.PointField(srid=4326)
	objects = models.GeoManager()


	def __str__(self):
		return self.name

	def isAvailable(self):
		if self.available == 1:
			return True
		else:
			return False

	def getOwner(self):
		return self.owner.last_name + ", " + self.owner.first_name


class Review(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	vahay = models.ForeignKey(Vahay, on_delete=models.CASCADE)
	content = models.CharField(max_length=500)
	when_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.username + " - " + self.content


class Image(models.Model):
	vahay = models.ForeignKey(Vahay, on_delete=models.CASCADE)
	link = models.CharField(max_length=1000)

	def __str__(self):
		return self.vahay.name + " - " + self.link







