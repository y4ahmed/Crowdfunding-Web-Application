# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0005_message_encrypt'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='time_created',
            field=models.TimeField(auto_now_add=True, default=datetime.datetime(2017, 5, 2, 4, 26, 8, 493012, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
