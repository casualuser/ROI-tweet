from django.db import models


class Message(models.Model):
    tweet = models.CharField(max_length=50)
    date = models.DateTimeField('date')
    name = models.CharField(max_length=20)