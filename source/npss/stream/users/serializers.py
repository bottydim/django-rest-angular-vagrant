from rest_framework import serializers

from stream.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'email',
                  'password',
                  'first_name',
                  'last_name',
                  'data_joined',
                  'last_login',
                  'last_login_ip')
        read_only_fields = ('id',)
