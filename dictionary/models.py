from django.db import models
from accounts.models import *


class dictionary(models.Model):
    firstName = models.CharField(max_length=100, blank=True, default='')
    color = models.CharField(max_length=100)
    shadow = models.IntegerField()
    shadowColor = models.IntegerField()
    border = models.IntegerField()
    creators = models.TextField()
    postNumber = models.IntegerField(null=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)


class post(models.Model):
    nickname = models.CharField(max_length=30, null=False, default="")
    consonant = models.CharField(max_length=10)
    contents = models.TextField()
    like = models.ManyToManyField(User, related_name='posts', blank=True)
    likes = models.BigIntegerField(default=0, null=True)
    dictionary = models.ForeignKey(
        dictionary, on_delete=models.CASCADE, related_name='post')
    is_liked = models.BooleanField(default=False)
