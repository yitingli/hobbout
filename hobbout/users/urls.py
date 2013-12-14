from django.conf.urls import patterns, include, url

from .views import TingUserCreateView, TingUserUpdateView, TingUserPasswordChangeView


urlpatterns = patterns('',

    url(r'^login/$', 'users.views.login', name='login'),
    url(r'^register/$', TingUserCreateView.as_view(), name='register'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'users/logged_out.html', 'next_page': '/'},
        name='logout'),
    url(r'^update/$', TingUserUpdateView.as_view(), name='user_update'),
    url(r'^password/change$', TingUserPasswordChangeView.as_view(), name='user_password_change'),

)
