from django.contrib import auth
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, resolve_url
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView
from django.views.generic.edit import FormMixin

from .models import TingUser
from .forms import TingUserCreateForm, TingUserLoginForm, TingUserUpdateForm, TingUserPasswordChangeForm


def login(request):
    if request.POST:
        form = TingUserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
        return render(request, 'users/login.html', {'form': form})
    else:
        form = TingUserLoginForm()
        return render(request, 'users/login.html', {'form': form})


class TingUserCreateView(CreateView):

    model = TingUser
    form_class = TingUserCreateForm
    template_name = 'users/create.html'

    #@Note: CreateView, UpdateView has built-in FormMixin
    def get_success_url(self):
        return reverse('user_home', kwargs={'username': self.username})

    #@Note: replace [if form.is_valid():]; redirects to get_success_url()
    def form_valid(self, form):
        form.save()
        user = auth.authenticate(username=form.cleaned_data['email'],
                                 password=form.cleaned_data['password'])
        if user is not None:
            auth.login(self.request, user)
            self.username = form.cleaned_data['username']
            return HttpResponseRedirect(self.get_success_url())
        else:
            return render(self.request, 'users/create.html', {'form': form, 'error_msg': 'create error'})


class TingUserUpdateView(UpdateView):

    model = TingUser
    form_class = TingUserUpdateForm
    template_name = 'users/update.html'

    def get_initial(self):
        self.initial['user'] = self.request.user
        return super(TingUserUpdateView, self).get_initial()

    #@Note: By default, it will get object from pk or slug
    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        super(TingUserUpdateView, self).form_valid(form)
        return render(self.request, 'users/update.html', {'form': form, 'update_success': True})


class TingUserPasswordChangeView(UpdateView):

    model = TingUser
    form_class = TingUserPasswordChangeForm
    template_name = 'users/password_change.html'

    #@Note: By default, it will get initial data from self.initial variable
    def get_initial(self):
        self.initial.update({'user': self.request.user})
        return super(TingUserPasswordChangeView, self).get_initial()

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('user_update')
