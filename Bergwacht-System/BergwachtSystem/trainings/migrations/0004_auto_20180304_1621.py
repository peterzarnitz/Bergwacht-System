# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-04 15:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0003_auto_20180220_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingCategory',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Ausbildungskategorie',
                'verbose_name_plural': 'Ausbildungskategorien',
            },
        ),
        migrations.AlterModelOptions(
            name='training',
            options={'verbose_name': 'Ausbildung', 'verbose_name_plural': 'Ausbildungen'},
        ),
        migrations.AddField(
            model_name='training',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trainings.TrainingCategory', verbose_name='Kategorie'),
        ),
    ]