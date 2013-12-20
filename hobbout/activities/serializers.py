from rest_framework import serializers

from .models import Activity, ActivityComment, UserActivityBridge


class ActivityCreateSerializer(serializers.ModelSerializer):

    group = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Activity
        depth = 1
        fields = ('name', 'content', 'group', 'start_time', 'end_time', 'place', 'capacity')

    def restore_object(self, attrs, instance=None):
        attrs['owner'] = self.context['user']
        activity = Activity(**attrs)
        return activity


class ActivityCommentCreateSerializer(serializers.ModelSerializer):

    activity = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = ActivityComment
        depth = 1
        fields = ('content', 'activity')

    def restore_object(self, attrs, instance=None):
        attrs['owner'] = self.context['user']
        comment = ActivityComment(**attrs)
        return comment


class UserActivityBridgeCreateSerializer(serializers.ModelSerializer):

    activity = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = UserActivityBridge
        depth = 1
        fields = ('activity', )

    def restore_object(self, attrs, instance=None):
        attrs['user'] = self.context['user']
        bridge = UserActivityBridge(**attrs)
        return bridge
