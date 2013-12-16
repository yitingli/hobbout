# core/api.py
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    """
    url(r'^noteboard/note/create/$', NoteCreateAPIView.as_view(), name='noteboard-note-create'),
    url(r'^user/(?P<pk>[0-9]+)/microblogs/$', MicroBlogListAPIView.as_view(), name='microblog-list'),
    url(r'^mediaframe/(?P<pk>[0-9]+)/rate/$', MediaFrameRateAPIView.as_view(), name='mediaframe-rate'),
    """
)
