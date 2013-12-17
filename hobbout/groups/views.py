from braces.views import LoginRequiredMixin
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView

from users.models import TingUser
from groups.models import Group, UserGroupBridge


class GroupNoticesView(DetailView):

    model = Group
    template_name = 'users/user_home.html'

    def get_context_data(self, **kwargs):
        context = super(GroupNoticesView, self).get_context_data(**kwargs)
        context['topics'] = self.object.get_notices()
        if self.request.user.is_authenticated():
            try:
                bridge = UserGroupBridge.objects.get(user=self.request.user, group=self.object)
                context['post_permission'] = bridge.role > 0
            except UserGroupBridge.DoesNotExist:
                pass
        context['post_permission'] = False
        context['topic_type'] = 'N'
        return context


class GroupDiscussionsView(DetailView):

    model = Group
    template_name = 'users/user_home.html'

    def get_context_data(self, **kwargs):
        context = super(GroupDiscussionsView, self).get_context_data(**kwargs)
        context['topics'] = self.object.get_discussions()
        context['post_permission'] = True
        context['topic_type'] = 'D'
        return context


class GroupActivitiesView(DetailView):

    model = Group
    template_name = 'users/user_home.html'

    def get_context_data(self, **kwargs):
        context = super(GroupActivitiesView, self).get_context_data(**kwargs)
        context['topics'] = self.object.get_activities()
        return context
