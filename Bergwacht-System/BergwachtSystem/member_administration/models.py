# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

STATUS_CHOICES = (
    ('AEK', 'Aktive Einsatzkraft'),
    ('ANW', 'Anwärter'),
    ('NEK', 'Nicht-aktive Einsatzkraft'),
)

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

    class Meta:
        verbose_name_plural = 'Mitglieder'
        ordering = ['status', 'user__last_name']

    def __str__(self):
        return self.user.username

    def isAnwaerter(self):
        return self.status == 'ANW'

    def isAEK(self):
        return self.status == 'AEK'

    # Calculate Age of a Member 
    def getAge(self):
        age = 0;
        today = date.today()
        if self.birthdate != None:
            age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age


# Qualifications of a Member
class Qualification(models.Model):
    name = models.CharField(primary_key=True, max_length=40, verbose_name='Name')

    class Meta:
        verbose_name_plural = 'Qualifikation'

    def __str__(self):
        return self.name


# Connection of Members and Qualifications
class MemberHasQualification(models.Model): 
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='Mitglied')
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE, verbose_name='Qualifikation')
    date = models.DateField(verbose_name='Datum', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Qualifikationen von Mitgliedern'

    def __str__(self):
        return self.member.user.username + '-' + self.qualification.name


# Creates a Member object if new User is created
@receiver(post_save, sender=User)
def create_member(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)
