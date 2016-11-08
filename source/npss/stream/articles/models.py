from django.db import models

from stream.categories.models import Category
from stream.contents.models import Content
from stream.pictures.models import Picture


class Article(Content):
    content = models.ForeignKey(Picture)
    category = models.ForeignKey(Category, null=True)
    text = models.TextField(max_length=10000, null=True, blank=False)

    def __str__(self):
        return 'Content: ' + self.content + '\r\n' + self.text
