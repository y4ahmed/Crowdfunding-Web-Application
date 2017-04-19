from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Report(models.Model):
    author = models.OneToOneField(User)
    title = models.CharField(max_length=255)
    compName = models.CharField(max_length=255)
    ceo = models.CharField(max_length=255)
    phoneNum = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    projects = models.TextField()
    private = models.BooleanField(default=False)
    files = models.FileField(upload_to='attachments')
    #time_created = models.DateTimeField(auto_now_add = True);
    time_created = models.TimeField(auto_now_add = True);
    #time_last_modified = models.DateTimeField(auto_now = True);
    folder = models.ForeignKey(Folder, blank=True, null=True);
    AES_key= models.CharField(max_length=500, blank=True)

class File(models.Model):
    title = models.CharField(max_length=128)
    file = models.FileField(upload_to='')
    report = models.OneToOneField(Report)
    hash_code = models.CharField(max_length=500, blank=True, null=True)


class Folder(models.Model):
    name = models.CharField(max_length=128)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.name