from rest_framework import generics

from stream.articles.models import Article
from stream.articles.serializers import ArticleSerializer


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetails(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_fields = ('id',)
