from django.db import models
from frontend.models import *
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    group_name = models.CharField(max_length=30,)
    member_list = models.ManyToManyField(BaseUser)
    report_list = []

    def add_members(self, mem_list):
        for mem in mem_list:
            try:
                user = User.objects.get(username__iexact=mem)
                base_user = BaseUser.objects.get(user=user)
                self.member_list.add(base_user)
            except User.DoesNotExist:
                # TODO: fix the error page redirection
                raise forms.ValidationError(_('Invalid receiver name. Try again.'), code='invalid')

    def add_reports(self, reports):
        for r in reports:
            self.report_list += [r]
