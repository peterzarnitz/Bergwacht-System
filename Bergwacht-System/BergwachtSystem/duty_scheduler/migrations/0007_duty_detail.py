# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-04 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duty_scheduler', '0006_auto_20180220_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='duty',
            name='detail',
            field=models.CharField(max_length=20, null=True, verbose_name='Detail'),
        ),
    ]
