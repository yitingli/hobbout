from rest_framework import serializers

from .models import Topic, TopicComment


class TopicCreateSerializer(serializers.ModelSerializer):

    group = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Topic
        depth = 1
        fields = ('name', 'content', 'group', 'topic_type')

    def restore_object(self, attrs, instance=None):
        attrs['owner'] = self.context['user']
        topic = Topic(**attrs)
        return topic


class TopicCommentCreateSerializer(serializers.ModelSerializer):

    topic = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = TopicComment
        depth = 1
        fields = ('content', 'topic')

    def restore_object(self, attrs, instance=None):
        attrs['owner'] = self.context['user']
        comment = TopicComment(**attrs)
        return comment
