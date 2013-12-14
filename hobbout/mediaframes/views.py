from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MediaFrame
from .forms import MediaFrameCreateForm, VideoFrameCreateForm
from .serializers import MediaFrameRateSerializer
from core.mixins import OwnerContextMixin, OwnerRequiredMixin


class MediaFrameCreateView(LoginRequiredMixin, OwnerContextMixin, OwnerRequiredMixin, CreateView):

    model = MediaFrame
    form_class = MediaFrameCreateForm
    template_name = 'mediaframes/create.html'

    def get_initial(self):
        self.initial['owner'] = self.request.user
        return super(MediaFrameCreateView, self).get_initial()

    def get_login_url(self):
        return reverse('login')

    def get_success_url(self):
        return self.object.album.get_absolute_url()


class VideoFrameCreateView(LoginRequiredMixin, OwnerContextMixin, OwnerRequiredMixin, CreateView):
    model = MediaFrame
    form_class = VideoFrameCreateForm
    template_name = 'mediaframes/video_create.html'

    def get_initial(self):
        self.initial['owner'] = self.request.user
        return super(VideoFrameCreateView, self).get_initial()

    def get_login_url(self):
        return reverse('login')

    def get_success_url(self):
        return self.object.album.get_absolute_url()


class MediaFrameDeleteView(LoginRequiredMixin, OwnerContextMixin, OwnerRequiredMixin, DeleteView):

    model = MediaFrame

    def get_success_url(self):
        return self.object.album.get_absolute_url()


class MediaFrameDetailView(OwnerContextMixin, DetailView):

    model = MediaFrame
    template_name = 'mediaframes/detail.html'


class MediaFrameRateAPIView(APIView):

    permission_classes = (permissions.AllowAny, )

    def post(self, request, pk, format=None):
        obj = get_object_or_404(MediaFrame, pk=pk)
        serializer = MediaFrameRateSerializer(data=request.DATA)
        if serializer.is_valid():
            if obj.rate_count == 0:
                obj.rating = serializer.object['rating']
            else:
                obj.rating = (obj.rating * obj.rate_count + serializer.object['rating']) / (obj.rate_count + 1)
            obj.rate_count += 1
            obj.save()
            return Response(data={'id': obj.pk, 'rating': "{0:.2f}".format(obj.rating)}, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
