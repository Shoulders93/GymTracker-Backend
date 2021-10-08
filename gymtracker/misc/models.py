from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Misc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=None)
    hours_slept = models.IntegerField(default=0)
    bodyweight = models.IntegerField(default=0)
    additional_notes = models.CharField(max_length=150)