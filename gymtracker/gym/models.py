from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Gym(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=None)
    exercise = models.CharField(max_length=45)
    sets = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)