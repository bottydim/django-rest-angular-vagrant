from django.db import models

from stream.users.models import User


class Comment(models.Model):
    text = models.TextField(max_length=5000, null=True, blank=False)
    owner = models.ForeignKey(User)

    # TODO article FK
    def __str__(self):
        return self.text
