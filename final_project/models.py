from django.db import models
from django.contrib.auth.models import User

class Match(models.Model):
    local = models.CharField(max_length=15)
    visitor = models.CharField(max_length=15)
    place = models.CharField(default='', max_length=20)
    date = models.DateTimeField()

    def __str__(self):
        return self.local +" x " + self.visitor
