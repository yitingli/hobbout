from django.db import models
from model_utils.models import TimeStampedModel

from annoying.fields import JSONField


class Activity(TimeStampedModel):

    name = models.CharField(max_length=255)
    content = models.TextField(default="", blank=True)
    owner = models.ForeignKey('users.TingUser')
    group = models.ForeignKey('groups.Group')

    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    place = models.CharField(max_length=255, default="", blank=True)

    comment_num = models.IntegerField(default=0, blank=True)

    participants = JSONField(null=True, blank=True)
    p_num = models.IntegerField(default=0, blank=True)


class ActivityComment(TimeStampedModel):

    content = models.TextField(default="", blank=True)
    owner = models.ForeignKey('users.TingUser')
    activity = models.ForeignKey('activities.Activity')
    parent_comment = models.ForeignKey('self', null=True, blank=True)
