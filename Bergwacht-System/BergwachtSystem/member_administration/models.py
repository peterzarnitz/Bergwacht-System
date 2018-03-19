# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
#from duty_scheduler.models import Dutyarea

STATUS_CHOICES = (
    ('AEK', 'Aktive Einsatzkraft'),
    ('ANW', 'Anwärter'),
    ('NEK', 'Nicht-aktive Einsatzkraft'),
)


class DutyGroup(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    # primary_duty_area = models.ForeignKey(Dutyarea, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Trupps'
        verbose_name = 'Trupp'

    def __unicode__(self):
        return self.name


# Defines am Member of the Bergwacht with personal data
class Member(models.Model):
    # Link to the user-profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Personal Data
    mobile = models.CharField(max_length=20, verbose_name='Handynummer', null=True, blank=True)
    adress_street = models.CharField(max_length=100, verbose_name='Straße & Hnr.', null=True, blank=True)
    adress_plz = models.CharField(max_length=6, verbose_name='PLZ', null=True, blank=True)
    adress_city = models.CharField(max_length=100, verbose_name='Stadt', null=True, blank=True)
    birthdate = models.DateField(verbose_name='Geburtsdatum', null=True, blank=True)
    bw_join = models.DateField(verbose_name='Bergwacht-Eintritt', null=True, blank=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='ANW')
    dutygroups = models.ManyToManyField(DutyGroup, through='Members_in_Dutygroup',
                                        through_fields=('member', 'dutygroup'), related_name='dutygroups')

    class Meta:
        verbose_name_plural = 'Mitglieder'
        ordering = ['status', 'user__last_name']

    def __unicode__(self):
        if not self.user.last_name:
            return self.user.username
        else:
            return self.user.last_name + ', ' + self.user.first_name

    def isAnwaerter(self):
        return self.status == 'ANW'

    def isAEK(self):
        return self.status == 'AEK'

    # Calculate Age of a Member 
    def getAge(self):
        age = 0;
        today = date.today()
        if self.birthdate != None:
            age = today.year - self.birthdate.year - (
                        (today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age


# Qualifications of a Member
class Qualification(models.Model):
    name = models.CharField(primary_key=True, max_length=40, verbose_name='Name')

    class Meta:
        verbose_name_plural = 'Qualifikation'

    def __unicode__(self):
        return self.name


# Connection of Members and Qualifications
class MemberHasQualification(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='Mitglied')
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE, verbose_name='Qualifikation')
    date = models.DateField(verbose_name='Datum', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Qualifikationen von Mitgliedern'

    def __unicode__(self):
        return self.member.user.username + '-' + self.qualification.name


class Members_in_Dutygroup(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='Mitglied')
    dutygroup = models.ForeignKey(DutyGroup, on_delete=models.CASCADE, verbose_name='Trupp')

    class Meta:
        verbose_name_plural = 'Truppmitgliedschaft'

    def __unicode__(self):
        return unicode(self.member) + '-' + unicode(self.dutygroup)


# Creates a Member object if new User is created
@receiver(post_save, sender=User)
def create_member(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)
