from rest_framework import generics
from television.pictures.models import Picture

from television.pictures.serializers import PictureSerializer


class PictureList(generics.ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class PictureDetail(generics.RetrieveDestroyAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    lookup_fields = ('id',)
