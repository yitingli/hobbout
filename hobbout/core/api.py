# core/api.py
from django.conf.urls import patterns, url

from topics.views import TopicCreateAPIView, TopicCommentCreateAPIView


urlpatterns = patterns('',

    url(r'^topic/create/$', TopicCreateAPIView.as_view(), name='topic-create'),
    url(r'^topic/comment/create/$', TopicCommentCreateAPIView.as_view(), name='comment-create'),

)
