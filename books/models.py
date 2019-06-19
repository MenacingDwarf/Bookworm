from django.db import models
from django.contrib.auth.models import User


class Reader(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    location = models.CharField(max_length=200)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(Reader, models.CASCADE, blank=True, null=True)
