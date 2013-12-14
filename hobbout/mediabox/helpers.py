import hashlib
from datetime import datetime
from os import path
from random import randint

from django.conf import settings
from django.utils.encoding import smart_str


def tokey(*args):
    """
    Computes a (hopefully) unique key from arguments given.
    Copied from sorl.thumbnail.helpers
    """
    salt = '||'.join([smart_str(arg) for arg in args])
    hash_ = hashlib.md5(salt)
    return hash_.hexdigest()


"""
def _get_thumbnail_filename(self, source, geometry_string, options):
        key = tokey(source.key, geometry_string, serialize(options))
        # make some subdirs
        path = '%s/%s/%s' % (key[:2], key[2:4], key)
        return '%s%s.%s' % (settings.THUMBNAIL_PREFIX, path,
                            EXTENSIONS[options['format']])
"""

def get_key(instance, filename):
    SECRET_KEY = 'Or3An6ge'
    fmt = "%Y%m%d%H%M%S%f"
    utc_now = datetime.utcnow().strftime(fmt)
    randnum = randint(10000, 99999)
    key = tokey(instance.owner.username, filename, utc_now, SECRET_KEY, str(randnum))
    return key


def upload_image_filename(instance, filename):
    """
    Used to upload images
    """
    _, extension = path.splitext(filename)
    key = get_key(instance, filename)
    return '%s/%s/%s/%s/%s%s' % (settings.IMAGE_PATH_PREFIX, key[:2], key[2:4], key[4:6], key, extension)


def upload_video_filename(instance, filename):
    """
    Used to upload video files
    """
    _, extension = path.splitext(filename)
    key = get_key(instance, filename)
    return '%s/%s/%s/%s/%s%s' % (settings.VIDEO_PATH_PREFIX, key[:2], key[2:4], key[4:6], key, extension)


def upload_file_filename(instance, filename):
    """
    Used to upload general files
    """
    _, extension = path.splitext(filename)
    key = get_key(instance, filename)
    return '%s/%s/%s/%s/%s%s' % (settings.FILE_PATH_PREFIX, key[:2], key[2:4], key[4:6], key, extension)
