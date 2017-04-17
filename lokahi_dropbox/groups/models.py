from django.db import models

# Create your models here.
class Group(models.Model):
    group_name = models.CharField(max_length=30,)
    member_list = [];
    report_list = [];

    def add_members(self, mem_list):
        for mem in mem_list:
            member_list += mem;
