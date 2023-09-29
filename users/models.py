from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


# Create your models here.
class Contr(models.Model):
    name = models.CharField('Ваш ответ',max_length=10,blank=True)
    otvet = models.CharField('Ответ', max_length=10)
    def __str__(self):
        return self.otvet
