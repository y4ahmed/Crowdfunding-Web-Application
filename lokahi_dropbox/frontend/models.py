from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from Crypto.PublicKey import RSA
#from reports.models import *
#Gonna fix,circular dependence from Reports->Groups->BaseUser->Reports

class BaseUser(models.Model):
    user = models.OneToOneField(User)
    user_role = models.CharField(max_length=30)
    RSAkey = models.CharField(max_length=10000)
    reports = models.ManyToManyField('reports.Report')

    def set_user_role(self, user_role):
        self.user_role = user_role
