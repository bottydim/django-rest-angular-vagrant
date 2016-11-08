from rest_framework import serializers

from stream.videos.models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id',
                  'title',
                  'description',
                  'views_count',
                  'created_on',
                  'owner',
                  'deleted_on',
                  'category')
        read_only_fields = ('id',)
