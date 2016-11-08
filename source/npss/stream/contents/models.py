from django.db import models

from television.comments.models import Comment
from television.users.models import User


class Content(models.Model):
    title = models.CharField(max_length=20, null=True, blank=False)
    description = models.TextField(max_length=200)
    views_count = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    deleted_on = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
