from django.conf import settings

from sorl.thumbnail.base import ThumbnailBackend


class CustomThumbnailBackend(ThumbnailBackend):

    def _get_thumbnail_filename(self, source, geometry_string, options):
        index = len(settings.IMAGE_PATH_PREFIX) + 1
        crop = options['crop']
        if crop:
            thumb_path = '%s/%s/%s' % (crop, geometry_string, source.name[index:])
        else:
            thumb_path = '%s/%s/%s' % ('nocrop', geometry_string, source.name[index:])
        return settings.THUMBNAIL_PATH_PREFIX + '/' + thumb_path
