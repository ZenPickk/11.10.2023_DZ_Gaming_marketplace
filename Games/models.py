from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    creator = models.TextField()
    genre = models.TextField()
    year = models.IntegerField()