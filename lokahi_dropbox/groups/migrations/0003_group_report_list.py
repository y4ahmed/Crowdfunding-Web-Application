# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20170501_2052'),
        ('groups', '0002_group_member_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='report_list',
            field=models.ManyToManyField(to='reports.Report'),
        ),
    ]
