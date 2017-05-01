import os
from django.db import models
from django.contrib.auth.models import User
from groups.models import Group


class Report(models.Model):
    owner = models.ForeignKey(User)
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
    # time_created = models.DateTimeField(auto_now_add = True);
    time_created = models.TimeField(auto_now_add=True)
    # time_last_modified = models.DateTimeField(auto_now = True);
    AES_key = models.CharField(max_length=500, blank=True)


class ReportPermissions(models.Model):
    report = models.OneToOneField(Report, on_delete=models.CASCADE,
                                  related_name='permissions')
    allowed_users = models.ManyToManyField(User, blank=True)
    allowed_groups = models.ManyToManyField(Group, blank=True)


def generate_file_path(instance, filename):
    return os.path.join(
        "reportFiles",
        instance.title.replace(" ", ""),
        filename.replace(" ", "")
    )


class File(models.Model):
    report = models.ForeignKey(Report)
    title = models.CharField(max_length=30)
    upload_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_encrypted = models.BooleanField(default=False)
    upload = models.FileField(upload_to=generate_file_path)

    def filename(self):
        return os.path.basename(self.file.name)


class CompanyDetails(models.Model):
    owner = models.OneToOneField(User)
    company_name = models.CharField(max_length=30)
    company_phone = models.CharField(max_length=30)
    company_location = models.CharField(max_length=30)
    # company_country = CountryField(blank_label='(Select Country)')#Look at
    # django countries for choices
