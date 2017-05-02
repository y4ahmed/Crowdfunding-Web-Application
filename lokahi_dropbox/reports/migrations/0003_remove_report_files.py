# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20170501_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='files',
        ),
    ]
