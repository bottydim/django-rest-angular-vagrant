from rest_framework import serializers

from television.comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'owner')
        read_only_fields = ('id',)
