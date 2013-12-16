from django.db import models
from model_utils.models import TimeStampedModel


class Topic(TimeStampedModel):

    name = models.CharField(max_length=255)
    content = models.TextField(default="", blank=True)
    owner = models.ForeignKey('users.TingUser')
    group = models.ForeignKey('groups.Group')


class TopicComment(TimeStampedModel):

    content = models.TextField(default="", blank=True)
    owner = models.ForeignKey('users.TingUser')
    topic = models.ForeignKey('topics.Topic')
    parent_comment = models.ForeignKey('self', null=True, blank=True)
