from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    first = models.CharField(max_length=60)
    last = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.first} {self.last}'
