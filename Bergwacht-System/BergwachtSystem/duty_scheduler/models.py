# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from member_administration.models import Member


class Dutyarea(models.Model):
    name = models.CharField(primary_key=True, max_length=40, verbose_name='Name')
    link = models.CharField(max_length=100, verbose_name='Link', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Dienstgebiete'
        verbose_name = 'Dienstgebiet'

    def __unicode__(self):
        return self.name.encode('utf-8')


class Dutycategory(models.Model):
    name = models.CharField(primary_key=True, max_length=40, verbose_name='Name')

    class Meta:
        verbose_name_plural = 'Dienstkategorien'
        verbose_name = 'Dienstkategorie'

    def __unicode__(self):
        return self.name.encode('utf-8')


class Dutyrole(models.Model):
    name = models.CharField(primary_key=True, max_length=40, verbose_name='Name')
    shortname = models.CharField(max_length=10, verbose_name='Kürzel')

    class Meta:
        verbose_name_plural = 'Dienstrollen'
        verbose_name = 'Dienstrolle'

    def __unicode__(self):
        return self.name.encode('utf-8')


# Defines a "Dienst" of the Bergwacht
class Duty(models.Model):
    duty_number = models.AutoField(primary_key=True, verbose_name='Dienstnummer')
    duty_area = models.ForeignKey(Dutyarea, on_delete=models.CASCADE, verbose_name='Dienstgebiet')
    duty_start = models.DateTimeField(verbose_name='Dienstbeginn')
    duty_end = models.DateTimeField(verbose_name='Dienstende')
    minaek = models.IntegerField(verbose_name='Geforderte AEK', blank=True, null=True)
    category = models.ForeignKey(Dutycategory, on_delete=models.CASCADE, null=True)
    detail = models.CharField(max_length=20, verbose_name='Detail', null=True, blank=True)

    members = models.ManyToManyField(Member, through='Takes_part_in_duty',
                                     through_fields=('duty', 'member'), )

    class Meta:
        verbose_name_plural = 'Dienste'
        verbose_name = 'Dienste'

    def __unicode__(self):
        return str(self.duty_number).encode('utf-8') + ' ' + str(self.duty_area.name).encode('utf-8')

    def getAEKcount(self):
        return self.members.filter(status='AEK').count()


class Takes_part_in_duty(models.Model):
    duty = models.ForeignKey(Duty, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    from_time = models.DateTimeField(verbose_name='Von')
    to_time = models.DateTimeField(verbose_name='Bis')
    function = models.ForeignKey(Dutyrole, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Funktion')
    comment = models.TextField(verbose_name='Kommentar', max_length=200, blank=True)

    class Meta:
        verbose_name_plural = 'Dienstteilnahmen'
        verbose_name = 'Dienstteilnahme'

    def __unicode__(self):
        return str(self.duty).encode('utf-8') + ' - ' + str(self.member.user.username).encode('utf-8')
