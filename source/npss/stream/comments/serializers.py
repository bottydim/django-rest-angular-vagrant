from rest_framework import serializers

from stream.comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'owner', 'picture', 'video', 'topic', 'article')
        read_only_fields = ('id',)
