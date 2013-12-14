from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404

from users.models import TingUser

class OwnerContextMixin(object):

    def dispatch(self, request, *args, **kwargs):
        self.owner_username = kwargs['username']
        self.owner = get_object_or_404(TingUser, username=self.owner_username)
        return super(OwnerContextMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(OwnerContextMixin, self).get_context_data(**kwargs)
        context['owner_username'] = self.owner_username
        context['owner'] = self.owner
        return context


class OwnerRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if request.user.username.lower() != kwargs['username'].lower():
            return HttpResponseForbidden()
        return super(OwnerRequiredMixin, self).dispatch(request, *args, **kwargs)
