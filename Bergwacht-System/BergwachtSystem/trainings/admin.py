# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Training, Prerequisites_for_training, TrainingCategory, TrainingEvent, Participates_in_trainingevent
from models import Possible_participates_in_trainingevent, Member_Trainings

admin.site.register(Training)
admin.site.register(Prerequisites_for_training)
admin.site.register(TrainingCategory)
admin.site.register(TrainingEvent)
admin.site.register(Member_Trainings)
admin.site.register(Participates_in_trainingevent)
admin.site.register(Possible_participates_in_trainingevent)

