from braces.views import LoginRequiredMixin
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView

from .models import Album
from .forms import AlbumCreateForm
from users.models import TingUser
from mediaframes.models import MediaFrame
from core.mixins import OwnerContextMixin, OwnerRequiredMixin
from core.pagination import AlbumPaginationMixin, MediaFramePaginationMixin


class AlbumListView(AlbumPaginationMixin, OwnerContextMixin, ListView):

    model = Album
    context_object_name = 'albums'
    template_name = 'albums/list.html'

    def get_queryset(self):
        self.owner = get_object_or_404(TingUser, username=self.owner_username)
        queryset = self.owner.get_albums(max_id=self.max_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AlbumListView, self).get_context_data(**kwargs)
        context['owner'] = self.owner
        context['private_albums'] = self.owner.get_albums(max_id=self.max_id, public=False)
        context['popular_frames'] = MediaFrame.objects.filter(owner=self.owner, album__is_public=True)\
                                    .order_by('-view_count')[:settings.PAGE_SIZE['POPULAR_SIDEBAR']]
        return context


class AlbumCreateView(LoginRequiredMixin, OwnerContextMixin, OwnerRequiredMixin, CreateView):

    model = Album
    form_class = AlbumCreateForm
    template_name = 'albums/create.html'

    def get_initial(self):
        self.initial['owner'] = self.request.user
        return super(AlbumCreateView, self).get_initial()

    def get_login_url(self):
        return reverse('login')

    def get_sucessful_url(self):
        return reverse('album:list', kwargs={'username': self.request.user})


class AlbumMediaFramesView(MediaFramePaginationMixin, OwnerContextMixin, ListView):

    model = MediaFrame
    context_object_name = 'mediaframes'
    template_name = 'mediaframes/list.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        self.owner = get_object_or_404(TingUser, username=self.owner_username)
        self.album = get_object_or_404(Album, owner=self.owner, slug=slug)
        queryset = self.album.get_media_frames(max_id=self.max_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AlbumMediaFramesView, self).get_context_data(**kwargs)
        context['owner'] = self.owner
        context['album'] = self.album
        return context
