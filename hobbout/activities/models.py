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

    capacity = models.IntegerField(default=0, blank=True)
    p_num = models.IntegerField(default=0, blank=True)

    def get_comments(self):
        comments = ActivityComment.objects.filter(activity=self).order_by('-created')
        return comments

    def get_available_num(self):
        return self.capacity-self.p_num

    def get_participants(self):
        users = UserActivityBridge.objects.filter(activity=self).order_by('-created').values_list('user__username', flat=True)
        return ', '.join(users)


class ActivityComment(TimeStampedModel):

    content = models.TextField(default="", blank=True)
    owner = models.ForeignKey('users.TingUser')
    activity = models.ForeignKey('activities.Activity')
    parent_comment = models.ForeignKey('self', null=True, blank=True)


class UserActivityBridge(TimeStampedModel):

    activity = models.ForeignKey('activities.Activity')
    user = models.ForeignKey('users.TingUser')

    class Meta:
        unique_together = (('user', 'activity'), )
