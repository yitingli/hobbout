from django.db import models
from model_utils.models import TimeStampedModel


class Topic(TimeStampedModel):

    name = models.CharField(max_length=255)
    content = models.TextField(default="", blank=True)
    topic_type = models.CharField(max_length=1, default='D')
    owner = models.ForeignKey('users.TingUser')
    group = models.ForeignKey('groups.Group')
    comment_num = models.IntegerField(default=0, blank=True)

    def __unicode__(self):
        return self.name

    def get_comments(self):
        comments = TopicComment.objects.filter(topic=self).order_by('-created')
        return comments


class TopicComment(TimeStampedModel):

    content = models.TextField(default="", blank=True)
    owner = models.ForeignKey('users.TingUser')
    topic = models.ForeignKey('topics.Topic')
    parent_comment = models.ForeignKey('self', null=True, blank=True)
