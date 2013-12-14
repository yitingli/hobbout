from django.db import models
from django.core.urlresolvers import reverse
from model_utils.models import TimeStampedModel

from core.utils import gen_float_decimal


class MediaFrame(TimeStampedModel):
    """
        Photo/Video Frame
    """

    TYPE_IMAGE = 'I'
    TYPE_VIDEO = 'V'

    album = models.ForeignKey('albums.Album')
    owner = models.ForeignKey('users.TingUser')
    description = models.CharField(max_length=500, default='', blank=True)
    """
        Simple solution is more straightforward than GenericForeignKey
        since we have only two types
    """
    content_type = models.CharField(max_length=1)
    image_item = models.ForeignKey('mediabox.MediaImage', null=True, blank=True)
    video_item = models.ForeignKey('mediabox.MediaVideo', null=True, blank=True)

    view_count = models.FloatField(default=gen_float_decimal, blank=True)
    rating = models.FloatField(default=5.0, blank=True)
    rate_count = models.IntegerField(default=0, blank=True)

    def __unicode__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('album:list', kwargs={'username': self.owner.username})

    def get_album_thumb_image_url(self):
        return self.image_item


class FrameComment(TimeStampedModel):

    owner = models.ForeignKey('users.TingUser')
    media_frame = models.ForeignKey('mediaframes.MediaFrame')
    content = models.CharField(max_length=180)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
