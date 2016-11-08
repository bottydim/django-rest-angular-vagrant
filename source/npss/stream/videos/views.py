from rest_framework import generics

from stream.videos.models import Video
from stream.videos.serializers import VideoSerializer


class VideoList(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoDetail(generics.RetrieveDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_fields = ('id',)
