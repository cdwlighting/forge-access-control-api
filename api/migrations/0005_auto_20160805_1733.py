# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-05 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20160805_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='macAddress',
            field=models.CharField(db_index=True, max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='cardToken',
            field=models.CharField(db_index=True, max_length=36, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='memberId',
            field=models.CharField(db_index=True, max_length=36, unique=True),
        ),
    ]
