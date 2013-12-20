from django.db.models import F
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ActivityCreateSerializer, ActivityCommentCreateSerializer
from core.permissions import PostNoticePermission


class ActivityCreateView(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, PostNoticePermission)

    def post(self, request, format=None):
        serializer = ActivityCreateSerializer(data=request.DATA, context={'user': request.user})
        if serializer.is_valid():
            self.check_object_permissions(request, serializer.object)
            serializer.save()
            return Response({
                                'id': serializer.object.pk,
                            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivityCommentCreateView(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def post(self, request, format=None):
        serializer = ActivityCommentCreateSerializer(data=request.DATA, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            serializer.object.topic.comment_num = F('comment_num') + 1
            serializer.object.topic.save()
            return Response({
                                'id': serializer.object.pk,
                            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)