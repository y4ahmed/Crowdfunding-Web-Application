# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_remove_baseuser_group_name'),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='member_list',
            field=models.ManyToManyField(to='frontend.BaseUser'),
        ),
    ]
