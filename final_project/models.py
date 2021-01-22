from django.db import models
from django.contrib.auth.models import User

class Match(models.Model):
    local = models.CharField(max_length=15)
    local_img = models.URLField(default='')

    visitor = models.CharField(max_length=15)
    visitor_img = models.URLField(default='')

    place = models.CharField(default='', max_length=50)
    date = models.CharField(default='', max_length=50)

    def __str__(self):
        return self.local +" x " + self.visitor
