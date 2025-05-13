from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.IntegerField(default=10)
    avatar = models.ImageField(upload_to='avatars/', default='default_avatar.jpg')
    email = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
