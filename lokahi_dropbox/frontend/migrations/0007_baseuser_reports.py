# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
        ('frontend', '0006_remove_baseuser_reports'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='reports',
            field=models.ManyToManyField(to='reports.Report'),
        ),
    ]
