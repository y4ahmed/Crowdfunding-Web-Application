# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_message_receiver'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.CharField(max_length=255, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(max_length=10000),
        ),
    ]
