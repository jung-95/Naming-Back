from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    userId = models.CharField(max_length=64)
    firstName = models.CharField(max_length=100)
