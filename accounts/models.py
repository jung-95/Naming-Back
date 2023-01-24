from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME = None
    userId = models.CharField(max_length=64, unique=True)
    firstName = models.CharField(max_length=100)
