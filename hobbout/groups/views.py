from braces.views import LoginRequiredMixin
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import TingUser
from groups.models import Group, UserGroupBridge
from .serializers import GroupCreateSerializer, UserGroupBridgeCreateSerializer


class GroupNoticesView(DetailView):

    model = Group
    template_name = 'users/user_home.html'

    def get_context_data(self, **kwargs):
        context = super(GroupNoticesView, self).get_context_data(**kwargs)
        context['topics'] = self.object.get_notices()
        context['topic_type'] = 'N'
        if self.request.user.is_authenticated():
            try:
                bridge = UserGroupBridge.objects.get(user=self.request.user, group=self.object)
                context['post_permission'] = bridge.role > 0
                return context
            except UserGroupBridge.DoesNotExist:
                pass
        context['post_permission'] = False
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
        context['topic_type'] = 'A'
        return context


class GroupAddView(TemplateView):

    template_name = 'groups/add.html'

    def get_context_data(self, **kwargs):
        context = super(GroupAddView, self).get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context


class GroupCreateAPIView(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def post(self, request, format=None):
        serializer = GroupCreateSerializer(data=request.DATA, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            bridge = UserGroupBridge(user=request.user, group=serializer.object, role=5)
            bridge.save()
            return Response({
                                'id': serializer.object.pk,
                            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserGroupBridgeCreateAPIView(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def post(self, request, format=None):
        serializer = UserGroupBridgeCreateSerializer(data=request.DATA, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({
                                'id': serializer.object.pk,
                            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
