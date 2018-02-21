# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from member_administration.models import Member
from trainings.models import Training


@login_required
def training_overview(request):
    training_list = Training.objects.order_by('name')
    return render(request, 'trainings/training_overview.html',
                  {'training_list': training_list, 'current_member': Member.objects.get(user=request.user)})