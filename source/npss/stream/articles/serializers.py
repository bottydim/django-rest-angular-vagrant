from rest_framework import serializers

from stream.articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'content', 'category', 'text')
        read_only_fields = ('id',)
