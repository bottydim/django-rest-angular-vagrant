from django.db import models

from television.roles.models import Role


class User(models.Model):
    username = models.CharField(max_length=15, null=True, blank=False)
    password = models.CharField(max_length=15, null=True, blank=False)
    email = models.EmailField(max_length=20, null=True, blank=False)
    first_name = models.CharField(max_length=15, null=True, blank=False)
    last_name = models.CharField(max_length=15, null=True, blank=False)
    data_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    last_login_ip = models.TextField(max_length=15, null=True)
    role = models.ForeignKey(Role, null=True)

    def __str__(self):
        return self.username + ' ' + self.first_name + ' ' + self.last_name
