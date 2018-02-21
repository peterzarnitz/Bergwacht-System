# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Training(models.Model):
    name = models.CharField(primary_key=True, max_length=50, verbose_name='Name')
    prerequisites = models.ManyToManyField("self", through='prerequisites_for_training',
                                           verbose_name='Voraussetzungen',
                                           symmetrical=False,
                                           related_name='with_prerequisite')

    class Meta:
        verbose_name_plural = 'Ausbildungen'

    def __str__(self):
        return self.name


class prerequisites_for_training(models.Model):
    pre_training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='pre_training',
                                     verbose_name='Voraussetzung')
    post_training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='post_training',
                                      verbose_name='Für Ausbildung')

    class Meta:
        verbose_name_plural = 'Ausbildungsvoraussetzungen'
        verbose_name = 'Ausbildungsvoraussetzung'

    def __str__(self):
        return str(self.pre_training) + ' > ' + str(self.post_training)
