from rest_framework import generics
from stream.pictures.models import Picture

from stream.pictures.serializers import PictureSerializer


class PictureList(generics.ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class PictureDetail(generics.RetrieveDestroyAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    lookup_fields = ('id',)
