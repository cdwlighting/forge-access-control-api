# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-04 23:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lockout',
            name='lockOutEndDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='memberId',
            field=models.CharField(default=django.utils.timezone.now, max_length=36, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='cardToken',
            field=models.CharField(max_length=36, unique=True),
        ),
    ]
