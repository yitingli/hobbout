# core/api.py
from django.conf.urls import patterns, url

from topics.views import TopicCreateAPIView, TopicCommentCreateAPIView
from activities.views import ActivityCreateAPIView, ActivityCommentCreateAPIView, UserActivityBridgeCreateAPIView
from groups.views import GroupCreateAPIView, UserGroupBridgeCreateAPIView


urlpatterns = patterns('',

    url(r'^topic/create/$', TopicCreateAPIView.as_view(), name='topic-create'),
    url(r'^topic/comment/create/$', TopicCommentCreateAPIView.as_view(), name='comment-create'),

    url(r'^activity/create/$', ActivityCreateAPIView.as_view(), name='activity-create'),
    url(r'^activity/comment/create/$', ActivityCommentCreateAPIView.as_view(), name='activity-comment-create'),
    url(r'^activity/participate/$', UserActivityBridgeCreateAPIView.as_view(), name='activity-participate'),

    url(r'^group/create/$', GroupCreateAPIView.as_view(), name='group-create'),
    url(r'^group/join/$', UserGroupBridgeCreateAPIView.as_view(), name='group-join'),

)
