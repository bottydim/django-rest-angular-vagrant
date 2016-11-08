from rest_framework import serializers

from stream.roles.models import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'title', 'owner')
        read_only_fields = ('id',)
