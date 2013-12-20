from rest_framework import serializers

from .models import Activity, ActivityComment


class ActivityCreateSerializer(serializers.ModelSerializer):

    group = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Activity
        depth = 1
        fields = ('name', 'content', 'group', 'start_time', 'end_time', 'place')

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
