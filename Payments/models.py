from django.db import models

# Create your models here.

class Payment(models.Model):
    username = models.TextField()
    amount_money = models.IntegerField()
    # comment = models.TextField(null = True, blank = True)

# Если вылазит ошибка с выбором:
# null = True, blank = True