from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView

from users.models import TingUser
from core.mixins import OwnerContextMixin


class HomeView(LoginRequiredMixin, TemplateView):

    template_name = 'users/user_home.html'
