from rest_framework import generics

from stream.roles.models import Role
from stream.roles.serializers import RoleSerializer


class RoleList(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleDetails(generics.RetrieveDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    lookup_fields = ('id',)
