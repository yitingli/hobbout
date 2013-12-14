from django.conf.urls import patterns, include, url

from .views import AlbumListView, AlbumCreateView, AlbumMediaFramesView


urlpatterns = patterns('',

    url(r'^$', AlbumListView.as_view(), name='list'),
    url(r'^create/$', AlbumCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[-_\w]+)/$', AlbumMediaFramesView.as_view(), name='mediaframes'),

)
