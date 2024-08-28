from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    friends = models.ManyToManyField('self', blank=True)

    def _str_(self):
        return self.username