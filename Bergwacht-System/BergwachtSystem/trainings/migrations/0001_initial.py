# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-18 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member_administration', '0003_auto_20180317_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participates_in_trainingevent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=200, verbose_name='Kommentar')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member_administration.Member')),
            ],
            options={
                'verbose_name': 'Teilnahme an Ausbildungstermin',
                'verbose_name_plural': 'Teilnahmen an Ausbildungstermin',
            },
        ),
        migrations.CreateModel(
            name='Possible_participates_in_trainingevent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=200, verbose_name='Kommentar')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member_administration.Member')),
            ],
            options={
                'verbose_name': 'M\xf6gliche Teilnahme an Ausbildungstermin',
                'verbose_name_plural': 'M\xf6gliche Teilnahmen an Ausbildungstermin',
            },
        ),
        migrations.CreateModel(
            name='Prerequisites_for_training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Ausbildungsvoraussetzung',
                'verbose_name_plural': 'Ausbildungsvoraussetzungen',
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Ausbildung',
                'verbose_name_plural': 'Ausbildungen',
            },
        ),
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
        migrations.CreateModel(
            name='TrainingEvent',
            fields=[
                ('training_event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_start', models.DateTimeField(verbose_name='Beginn')),
                ('event_end', models.DateTimeField(verbose_name='Ende')),
                ('max_member', models.IntegerField(verbose_name='Max. Teilnehmerzahl')),
                ('direct_registration', models.BooleanField(default=True, verbose_name='Direktanmeldung m\xf6glich')),
                ('participants', models.ManyToManyField(related_name='participants', through='trainings.Participates_in_trainingevent', to='member_administration.Member')),
                ('possible_participants', models.ManyToManyField(related_name='possible_participants', through='trainings.Possible_participates_in_trainingevent', to='member_administration.Member')),
                ('trainer', models.ManyToManyField(related_name='trainer', to='member_administration.Member')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainings.Training', verbose_name='Ausbildung')),
            ],
            options={
                'verbose_name': 'Ausbildungstermin',
                'verbose_name_plural': 'Ausbildungstermine',
            },
        ),
        migrations.AddField(
            model_name='training',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trainings.TrainingCategory', verbose_name='Kategorie'),
        ),
        migrations.AddField(
            model_name='training',
            name='prerequisites',
            field=models.ManyToManyField(related_name='with_prerequisite', through='trainings.Prerequisites_for_training', to='trainings.Training', verbose_name='Voraussetzungen'),
        ),
        migrations.AddField(
            model_name='prerequisites_for_training',
            name='post_training',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_training', to='trainings.Training', verbose_name='F\xfcr Ausbildung'),
        ),
        migrations.AddField(
            model_name='prerequisites_for_training',
            name='pre_training',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pre_training', to='trainings.Training', verbose_name='Voraussetzung'),
        ),
        migrations.AddField(
            model_name='possible_participates_in_trainingevent',
            name='trainingevent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainings.TrainingEvent'),
        ),
        migrations.AddField(
            model_name='participates_in_trainingevent',
            name='trainingevent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainings.TrainingEvent'),
        ),
    ]
