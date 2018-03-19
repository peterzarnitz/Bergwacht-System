# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-19 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('member_administration', '0004_auto_20180318_1422'),
        ('trainings', '0003_auto_20180319_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member_Trainings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member_administration.Member', verbose_name='Mitglied')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainings.Training', verbose_name='Ausbildung')),
            ],
            options={
                'verbose_name_plural': 'Ausbildung von Mitgliedern',
            },
        ),
        migrations.AlterField(
            model_name='possible_participates_in_trainingevent',
            name='first_register_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Erste Anmeldung'),
        ),
    ]