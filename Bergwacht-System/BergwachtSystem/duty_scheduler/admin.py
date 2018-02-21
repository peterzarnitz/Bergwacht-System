# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Duty, Dutyarea, Dutycategory, Takes_part_in_duty, Dutyrole

admin.site.register(Duty)
admin.site.register(Dutyarea)
admin.site.register(Dutycategory)
admin.site.register(Takes_part_in_duty)
admin.site.register(Dutyrole)