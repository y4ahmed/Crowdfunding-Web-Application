# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0004_message_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='encrypt',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
