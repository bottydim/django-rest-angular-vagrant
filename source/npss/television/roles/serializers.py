from rest_framework import serializers

from television.roles.models import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'title')
        read_only_fields = ('id',)
