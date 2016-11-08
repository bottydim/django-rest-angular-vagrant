from django.db import models
from stream.categories.models import Category

from stream.contents.models import Content


class Video(Content):
    category = models.ForeignKey(Category, null=True)
