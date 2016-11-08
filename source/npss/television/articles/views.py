from rest_framework import generics

from television.articles.models import Article
from television.articles.serializers import ArticleSerializer


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_fields = ('id',)
