from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView

from users.models import TingUser
from core.mixins import OwnerContextMixin


"""
class HomeView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['background_image_url'] = None
        return context
"""


class HomeView(RedirectView):

    url = '/yiting/'


class UserHomeView(OwnerContextMixin, TemplateView):

    template_name = 'users/user_home.html'

    def get_context_data(self, **kwargs):
        context = super(UserHomeView, self).get_context_data(**kwargs)
        self.owner = get_object_or_404(TingUser, username=self.kwargs['username'])
        context['owner'] = self.owner
        return context
