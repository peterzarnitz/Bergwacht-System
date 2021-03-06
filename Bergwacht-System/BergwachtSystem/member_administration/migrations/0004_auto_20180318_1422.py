# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-18 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_administration', '0003_auto_20180317_0923'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dutygroup',
            options={'verbose_name': 'Trupp', 'verbose_name_plural': 'Trupps'},
        ),
        migrations.AlterField(
            model_name='member',
            name='dutygroups',
            field=models.ManyToManyField(related_name='dutygroups', through='member_administration.Members_in_Dutygroup', to='member_administration.DutyGroup'),
        ),
    ]
