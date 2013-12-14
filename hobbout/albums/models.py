from django.db import models
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.conf import settings
from model_utils.models import TimeStampedModel
from slugify import slugify

from mediaframes.models import MediaFrame


class Album(TimeStampedModel):

    owner = models.ForeignKey('users.TingUser')
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    cover = models.ForeignKey('mediaframes.MediaFrame', null=True, blank=True, related_name='cover')
    description = models.CharField(max_length=255, blank=True)

    is_public = models.BooleanField(default=True)

    rank = models.FloatField(default=100.0, blank=True)

    class Meta:
        unique_together = (('owner', 'slug'), )

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Album, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('album:mediaframes', kwargs={'username': self.owner.username, 'slug': self.slug})

    def get_media_frames(self, max_id, size=settings.PAGE_SIZE['MEDIAFRAME']):
        criteria = Q(album=self)
        if max_id:
            criteria = criteria & Q(pk__lt=max_id)
        return MediaFrame.objects.filter(criteria).order_by('-rating', '-created')[:size]

    def get_album_thumb_frames(self):
        mediaframes = MediaFrame.objects.filter(album=self).order_by('-rating', '-created')[:4]
        frame_list = list(mediaframes)
        while len(frame_list) < 4:
            frame_list.append(None)
        return frame_list
