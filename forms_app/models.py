from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.CharField(max_length=500)
    timeCook = models.IntegerField()

    def __str__(self):
        return self.name
