from django.db.models import F
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserActivityBridge
from .serializers import ActivityCreateSerializer, ActivityCommentCreateSerializer, UserActivityBridgeCreateSerializer


class ActivityCreateAPIView(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def post(self, request, format=None):
        serializer = ActivityCreateSerializer(data=request.DATA, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            bridge = UserActivityBridge(user=request.user, activity=serializer.object)
            bridge.save()
            return Response({
                                'id': serializer.object.pk,
                            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivityCommentCreateAPIView(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def post(self, request, format=None):
        serializer = ActivityCommentCreateSerializer(data=request.DATA, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            serializer.object.activity.comment_num = F('comment_num') + 1
            serializer.object.activity.save()
            return Response({
                                'id': serializer.object.pk,
                            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserActivityBridgeCreateAPIView(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def post(self, request, format=None):
        serializer = UserActivityBridgeCreateSerializer(data=request.DATA, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            serializer.object.activity.p_num = F('p_num') + 1
            serializer.object.activity.save()
            return Response({
                                'id': serializer.object.pk,
                            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
