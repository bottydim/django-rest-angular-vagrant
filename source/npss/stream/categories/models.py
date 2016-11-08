from django.db import models

from stream.articles.models import Article
from stream.users.models import User


class Category(models.Model):
    title = models.CharField(max_length=15, null=True, blank=False)
    description = models.CharField(max_length=15)
    owner = models.ForeignKey(User)
    article = models.ForeignKey(Article, null=True)

    def __str__(self):
        return self.title
