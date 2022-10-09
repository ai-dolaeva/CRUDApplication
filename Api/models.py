from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Modification the inherited AbstractUser model
    """
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(blank=False, max_length=128)
    first_name = models.CharField(blank=True, max_length=30)

    def __str__(self):
        return self.username
