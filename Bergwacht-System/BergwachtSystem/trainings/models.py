# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models
from member_administration.models import Member


class TrainingCategory(models.Model):
    name = models.CharField(primary_key=True, max_length=50, verbose_name='Name')

    class Meta:
        verbose_name_plural = 'Ausbildungskategorien'
        verbose_name = 'Ausbildungskategorie'

    def __unicode__(self):
        return self.name


class Training(models.Model):
    name = models.CharField(primary_key=True, max_length=50, verbose_name='Name')
    prerequisites = models.ManyToManyField("self", through='Prerequisites_for_training',
                                           through_fields=('post_training', 'pre_training'),
                                           verbose_name='Voraussetzungen',
                                           symmetrical=False,
                                           related_name='with_prerequisite')
    category = models.ForeignKey(TrainingCategory, on_delete=models.CASCADE, verbose_name='Kategorie', null=True)

    class Meta:
        verbose_name_plural = 'Ausbildungen'
        verbose_name = 'Ausbildung'

    def __unicode__(self):
        return self.name


class Prerequisites_for_training(models.Model):
    pre_training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='pre_training',
                                     verbose_name='Voraussetzung', null=True)
    post_training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='post_training',
                                      verbose_name='Für Ausbildung', null=True)

    class Meta:
        verbose_name_plural = 'Ausbildungsvoraussetzungen'
        verbose_name = 'Ausbildungsvoraussetzung'

    def __unicode__(self):
        return unicode(self.pre_training) + ' > ' + unicode(self.post_training)


class TrainingEvent(models.Model):
    training_event_id = models.AutoField(primary_key=True)
    training = models.ForeignKey(Training, verbose_name='Ausbildung')
    event_start = models.DateTimeField(verbose_name='Beginn')
    event_end = models.DateTimeField(verbose_name='Ende')
    max_member = models.IntegerField(verbose_name='Max. Teilnehmerzahl')

    direct_registration = models.BooleanField(verbose_name="Direktanmeldung möglich", default=True)

    trainer = models.ManyToManyField(Member, related_name='trainer')
    participants = models.ManyToManyField(Member, through='Participates_in_trainingevent',
                                          through_fields=('trainingevent', 'member'), related_name='participants')
    possible_participants = models.ManyToManyField(Member, through='Possible_participates_in_trainingevent',
                                                   through_fields=('trainingevent', 'member'),
                                                   related_name='possible_participants')

    class Meta:
        verbose_name_plural = 'Ausbildungstermine'
        verbose_name = 'Ausbildungstermin'

    def __unicode__(self):
        return unicode(self.training.name) + ' - ' + unicode(self.event_start)

    def getMemberCount(self):
        return self.participants.count()


class Participates_in_trainingevent(models.Model):
    trainingevent = models.ForeignKey(TrainingEvent, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Kommentar', max_length=200, blank=True)
    first_register_timestamp = models.DateTimeField(verbose_name='Erste Anmeldung', editable=True, null=True)

    class Meta:
        verbose_name_plural = 'Teilnahmen an Ausbildungstermin'
        verbose_name = 'Teilnahme an Ausbildungstermin'

    def __unicode__(self):
        return unicode(self.trainingevent) + ' - ' + unicode(self.member)


class Possible_participates_in_trainingevent(models.Model):
    trainingevent = models.ForeignKey(TrainingEvent, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Kommentar', max_length=200, blank=True)
    first_register_timestamp = models.DateTimeField(default=timezone.now, verbose_name='Erste Anmeldung', editable=True,
                                                    null=True)

    class Meta:
        verbose_name_plural = 'Mögliche Teilnahmen an Ausbildungstermin'
        verbose_name = 'Mögliche Teilnahme an Ausbildungstermin'

    def __unicode__(self):
        return 'P - ' + unicode(self.trainingevent) + ' - ' + unicode(self.member)


class Member_Trainings(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='Mitglied')
    training = models.ForeignKey(Training, on_delete=models.CASCADE, verbose_name='Ausbildung')
    date = models.DateField(verbose_name='Datum', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Ausbildungen von Mitgliedern'
        verbose_name = 'Ausbildung von Mitglied'

    def __unicode__(self):
        return unicode(self.member) + '-' + unicode(self.training)