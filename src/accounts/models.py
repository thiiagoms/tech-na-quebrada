from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(
        upload_to='img_volunteers',
        null=True,
        default=True
    )

    def __str__(self):
        return f"{self.user.username} Profile"
