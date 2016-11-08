from django.db import models

from stream.users.models import User


class Category(models.Model):
    title = models.CharField(max_length=15, null=True, blank=False)
    description = models.CharField(max_length=15)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.title
