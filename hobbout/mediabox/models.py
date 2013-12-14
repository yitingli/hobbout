from django.db import models
from model_utils.models import TimeStampedModel
from sorl.thumbnail import get_thumbnail

from .helpers import upload_image_filename, upload_file_filename, upload_video_filename


class MediaBase(TimeStampedModel):

    owner = models.ForeignKey('users.TingUser')
    link = models.URLField(default='', blank=True)

    class Meta:
        abstract = True


class MediaImage(MediaBase):

    extension = models.CharField(max_length=10, default='', blank=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(upload_to=upload_image_filename, width_field='width',
                              height_field='height')

    def get_image(self, geometry, crop='center'):
        if crop:
            thumbnail = get_thumbnail(self.image, geometry, crop=crop)
        else:
            thumbnail = get_thumbnail(self.image, geometry)
        return thumbnail

    def get_image_url(self, geometry, crop='center'):
        image = self.get_image(geometry, crop)
        return image.url

    def get_image_size(self, geometry, crop='no_crop'):
        if 'x' in geometry:
            components = geometry.split('x')
            width = int(components[0])
            height = int(components[1])
            if self.width <= width and self.height <= height:
                return (self.width, self.height)

            if crop == 'no_crop':
                ratio = float(height) / float(width)
                image_ratio = float(self.height) / float(self.width)
                if image_ratio <= ratio:
                    return (width, int(width*image_ratio))
                else:
                    return (int(height/image_ratio), height)
        else:
            width = int(geometry)
            if self.width <= width:
                return (self.width, self.height)
            else:
                image_ratio = float(self.height) / float(self.width)
                return (width, int(width*image_ratio))

        return (width, height)


class MediaVideo(MediaBase):

    video_code = models.CharField(max_length=255, default='', blank=True)
    video = models.FileField(upload_to=upload_video_filename, null=True, blank=True)
    extension = models.CharField(max_length=10, default='', blank=True)


class MediaFile(MediaBase):

    title = models.CharField(max_length=50, default='Untitled', blank=True)
    doc = models.FileField(upload_to=upload_file_filename)
    rank = models.FloatField(default=100.0, blank=True)
    is_public = models.BooleanField(default=False)
