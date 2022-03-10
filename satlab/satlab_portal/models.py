from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    verified = models.IntegerField
    image_link = models.CharField(max_length=500)
    postfeed = models.CharField(max_length=1000)
    def __str__(self):
        return self.name





    