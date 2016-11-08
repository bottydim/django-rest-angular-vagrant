from rest_framework import generics

from television.videos.models import Video
from television.videos.serializers import VideoSerializer


class VideoList(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoDetail(generics.RetrieveDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_fields = ('id',)
