from django.db import models
from model_utils.models import TimeStampedModel
from slugify import slugify

from topics.models import Topic
from activities.models import Activity


class Group(TimeStampedModel):

    owner = models.ForeignKey('users.TingUser')
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    is_public = models.BooleanField(default=True)
    brief_description = models.CharField(max_length=255, blank=True)
    description = models.TextField(default="", blank=True)

    avatar = models.ForeignKey('mediabox.MediaImage', null=True, blank=True, on_delete=models.SET_NULL)

    area = models.ForeignKey('locations.Area')
    location = models.ForeignKey('locations.Location', null=True, blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Group, self).save(*args, **kwargs)

    def get_notices(self):
        topics = Topic.objects.filter(group=self, topic_type='N').order_by('-modified')
        return topics

    def get_discussions(self):
        discussions = Topic.objects.filter(group=self, topic_type='D').order_by('-modified')
        return discussions

    def get_activities(self):
        activities = Activity.objects.filter(group=self).order_by('-modified')
        return activities


class UserGroupBridge(TimeStampedModel):

    user = models.ForeignKey('users.TingUser')
    group = models.ForeignKey('groups.Group')
    alias = models.CharField(max_length=30, default="", blank=True)
    role = models.IntegerField(default=0, blank=True)
    post_num = models.IntegerField(default=0, blank=True)
    points = models.IntegerField(default=0, blank=True)

    class Meta:
        unique_together = (('user', 'group'), )
