from django.db import models

# Create your models here.

class User(models.Model):
    usermame = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    pasword = models.TextField()
     
