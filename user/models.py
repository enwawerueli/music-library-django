from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_image = models.FileField()

    def __str__(self):
        return self.user.username
