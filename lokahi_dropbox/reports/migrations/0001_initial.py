# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=128)),
                ('file', models.FileField(upload_to='')),
                ('hash_code', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('compName', models.CharField(max_length=255)),
                ('ceo', models.CharField(max_length=255)),
                ('phoneNum', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=255)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('sector', models.CharField(max_length=255)),
                ('projects', models.TextField()),
                ('private', models.BooleanField(default=False)),
                ('files', models.FileField(upload_to='attachments')),
                ('time_created', models.TimeField(auto_now_add=True)),
                ('AES_key', models.CharField(blank=True, max_length=500)),
                ('author', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='report',
            field=models.OneToOneField(to='reports.Report'),
        ),
    ]
