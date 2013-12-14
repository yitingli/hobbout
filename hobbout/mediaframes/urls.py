from django.conf.urls import patterns, include, url

from .views import MediaFrameCreateView, MediaFrameDetailView, VideoFrameCreateView, MediaFrameDeleteView


urlpatterns = patterns('',

    url(r'^create/$', MediaFrameCreateView.as_view(), name='create'),
    url(r'^create-video/$', VideoFrameCreateView.as_view(), name='video_create'),
    url(r'^(?P<pk>[0-9]+)/$', MediaFrameDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/delete/$', MediaFrameDeleteView.as_view(), name='delete'),

)
