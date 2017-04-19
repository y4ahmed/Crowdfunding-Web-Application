# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_remove_baseuser_group_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='RSAkey',
            field=models.CharField(max_length=10000, default=0),
            preserve_default=False,
        ),
    ]
