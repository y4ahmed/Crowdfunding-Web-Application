from django.db import models

# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length=10000,)
    receiver = models.CharField(max_length=255,)
    sender = models.CharField(max_length=255,)
    subject = models.CharField(max_length=30, default='subj')
    encrypt = models.BooleanField()
