from rest_framework import generics

from television.topics.models import Topic
from television.topics.serializers import TopicSerializer


class TopicList(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicDetail(generics.RetrieveDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_fields = ('id',)
