from django import template
from django.conf import settings


register = template.Library()


@register.simple_tag
def get_avatar(obj, geometry, crop='center'):
    if crop == 'no_crop':
        return obj.get_avatar_url(geometry, None)
    return obj.get_avatar_url(geometry, crop)


@register.simple_tag
def default_avatar(geometry):
    return settings.DEFAULT_AVATAR_LOCATION + geometry + '.jpg'
