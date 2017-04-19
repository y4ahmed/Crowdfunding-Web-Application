from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from Crypto.PublicKey import RSA
# Create your models here.


class BaseUser(models.Model):
    user = models.OneToOneField(User)
    user_role = models.CharField(max_length=30)
    RSAkey = models.CharField(max_length=10000)

    def set_user_role(self, user_role):
        self.user_role = user_role
