from django.db import models

from stream.users.models import User


class Role(models.Model):
    title = models.CharField(max_length=15, null=True)
    owner = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.title
