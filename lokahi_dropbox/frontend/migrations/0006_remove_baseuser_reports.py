# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_baseuser_reports'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseuser',
            name='reports',
        ),
    ]
