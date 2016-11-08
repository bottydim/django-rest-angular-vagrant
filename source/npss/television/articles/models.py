from django.db import models

from television.categories.models import Category
from television.contents.models import Content
from television.pictures.models import Picture


class Article(Content):
    content = models.ForeignKey(Picture)
    category = models.ForeignKey(Category, null=True)
    text = models.TextField(max_length=10000, null=True, blank=False)

    def __str__(self):
        return 'Content: ' + self.content + '\r\n' + self.text
