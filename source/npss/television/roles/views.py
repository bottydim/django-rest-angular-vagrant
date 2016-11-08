from rest_framework import generics

from television.roles.models import Role
from television.roles.serializers import RoleSerializer


class RoleList(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleDetail(generics.RetrieveDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    lookup_fields = ('id',)