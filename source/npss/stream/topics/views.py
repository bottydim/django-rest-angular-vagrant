from rest_framework import generics

from stream.topics.models import Topic
from stream.topics.serializers import TopicSerializer


class TopicList(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicDetails(generics.RetrieveDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_fields = ('id',)
