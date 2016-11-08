from rest_framework import generics

from stream.users.models import User
from stream.users.serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_fields = ('id',)
