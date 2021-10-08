from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=None)
    breakfast = models.CharField(max_length=45)
    lunch = models.CharField(max_length=100)
    dinner = models.CharField(max_length=100)