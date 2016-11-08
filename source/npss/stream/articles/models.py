from django.db import models

from stream.contents.models import Content


class Article(Content):
    text = models.TextField(max_length=10000, null=True, blank=False)

    def __str__(self):
        return 'Content: ' + self.content + '\r\n' + self.text
