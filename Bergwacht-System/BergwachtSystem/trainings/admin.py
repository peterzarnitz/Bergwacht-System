# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Training, prerequisites_for_training

admin.site.register(Training)
admin.site.register(prerequisites_for_training)
