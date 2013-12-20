from rest_framework import serializers

from .models import Group, UserGroupBridge


class GroupCreateSerializer(serializers.ModelSerializer):

    group = serializers.PrimaryKeyRelatedField()
    area = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Group
        depth = 1
        fields = ('name', 'brief_description', 'description', 'area')

    def restore_object(self, attrs, instance=None):
        attrs['owner'] = self.context['user']
        group = Group(**attrs)
        return group


class UserGroupBridgeCreateSerializer(serializers.ModelSerializer):

    group = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = UserGroupBridge
        depth = 1
        fields = ('group', )

    def restore_object(self, attrs, instance=None):
        attrs['user'] = self.context['user']
        bridge = UserGroupBridge(**attrs)
        return bridge
