# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-04 18:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('duty_scheduler', '0007_duty_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duty',
            name='detail',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Detail'),
        ),
        migrations.AlterField(
            model_name='takes_part_in_duty',
            name='function',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='duty_scheduler.Dutyrole', verbose_name='Funktion'),
        ),
    ]