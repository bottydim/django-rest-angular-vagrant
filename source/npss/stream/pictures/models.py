# Create your models here.
from django.db import models

from stream.articles.models import Article
from stream.contents.models import Content


class Picture(Content):
    article = models.ForeignKey(Article, null=True)
