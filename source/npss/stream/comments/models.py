from django.db import models

from stream.articles.models import Article
from stream.pictures.models import Picture
from stream.topics.models import Topic
from stream.users.models import User
from stream.videos.models import Video


class Comment(models.Model):
    text = models.TextField(max_length=5000, null=True, blank=False)
    owner = models.ForeignKey(User)
    picture = models.ForeignKey(Picture, null=True)
    video = models.ForeignKey(Video, null=True)
    topic = models.ForeignKey(Topic, null=True)
    article = models.ForeignKey(Article, null=True)

    # TODO article FK
    def __str__(self):
        return self.text
