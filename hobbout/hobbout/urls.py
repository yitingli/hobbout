from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from .views import HomeView


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^api/', include('core.api', namespace='api')),
    url(r'^rest/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^ckeditor/', include('ckeditor.urls')),

    url(r'^accounts/', include('users.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^group/(?P<pk>[0-9]+)/', include('groups.urls', namespace='group')),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    )

"""
reserved_word is used to validate username to avoid conflict with existing url patterns
"""
import re

url_splitor = re.compile(r'/|\$|\^|\\b')


def get_reserved_words(url_list):
    reserved_words = []
    for item in url_list:
        url_components = url_splitor.split(item.regex.pattern)
        if len(url_components) > 1:
            reserved_words.append(url_components[1])
    reserved_words = list(set(reserved_words))
    print reserved_words
    return reserved_words

reserved_words = get_reserved_words(urlpatterns)
