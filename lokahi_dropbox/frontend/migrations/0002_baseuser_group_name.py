# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='group_name',
            field=models.CharField(max_length=30, default=0),
            preserve_default=False,
        ),
    ]
