from django.db import models
from model_utils.models import TimeStampedModel


class Area(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(default="", blank=True)

    def __unicode__(self):
        return self.name


class Location(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(default="", blank=True)
    area = models.ForeignKey('locations.Area')

    def __unicode__(self):
        return self.name
