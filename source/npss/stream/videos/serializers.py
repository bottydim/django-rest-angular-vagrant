from rest_framework import serializers

from television.videos.models import Video


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
                  'comment',
                  'category')
        read_only_fields = ('id',)
