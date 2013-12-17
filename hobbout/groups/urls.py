from django.conf.urls import patterns, include, url

from .views import GroupNoticesView, GroupDiscussionsView, GroupActivitiesView

urlpatterns = patterns('',

    url(r'^notices/$', GroupNoticesView.as_view(), name='notices'),
    url(r'^discussions/$', GroupDiscussionsView.as_view(), name='discussions'),
    url(r'^activities/$', GroupActivitiesView.as_view(), name='activities'),

)
