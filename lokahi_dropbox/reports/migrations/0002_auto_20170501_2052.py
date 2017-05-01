# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import reports.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_member_list'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('company_phone', models.CharField(max_length=30)),
                ('company_location', models.CharField(max_length=30)),
                ('owner', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReportPermissions',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('allowed_groups', models.ManyToManyField(to='groups.Group', blank=True)),
                ('allowed_users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='file',
            name='file',
        ),
        migrations.RemoveField(
            model_name='file',
            name='hash_code',
        ),
        migrations.RemoveField(
            model_name='report',
            name='author',
        ),
        migrations.AddField(
            model_name='file',
            name='is_encrypted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='upload',
            field=models.FileField(upload_to=reports.models.generate_file_path, default=datetime.datetime(2017, 5, 1, 20, 51, 58, 58350, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 1, 20, 52, 6, 626743, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='report',
            field=models.ForeignKey(to='reports.Report'),
        ),
        migrations.AlterField(
            model_name='file',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.AddField(
            model_name='reportpermissions',
            name='report',
            field=models.OneToOneField(to='reports.Report', related_name='permissions'),
        ),
    ]
