# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_baseuser_group_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseuser',
            name='group_name',
        ),
    ]
