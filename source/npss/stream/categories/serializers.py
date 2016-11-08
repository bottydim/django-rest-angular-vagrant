from rest_framework import serializers

from television.categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'owner')
        read_only_fields = ('id',)