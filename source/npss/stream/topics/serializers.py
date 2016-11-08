from rest_framework import serializers

from stream.topics.models import Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id',
                  'title',
                  'description',
                  'views_count',
                  'created_on',
                  'owner',
                  'deleted_on',
                  'comment')
        read_only_fields = ('id',)
