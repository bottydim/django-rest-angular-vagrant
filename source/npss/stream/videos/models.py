from django.db import models
from television.categories.models import Category

from television.contents.models import Content


class Video(Content):
    category = models.ForeignKey(Category, null=True)
