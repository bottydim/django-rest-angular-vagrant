from rest_framework import generics

from stream.comments.models import Comment
from stream.comments.serializers import CommentSerializer


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetails(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_fields = ('id',)
