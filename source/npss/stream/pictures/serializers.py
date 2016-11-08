from rest_framework import serializers


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id',
                  'title',
                  'description',
                  'views_count',
                  'created_on',
                  'owner',
                  'deleted_on',
                  'article')
        read_only_fields = ('id',)
