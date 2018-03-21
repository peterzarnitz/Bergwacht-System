# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render

from .models import Member, User, Qualification, MemberHasQualification
from trainings.models import TrainingCategory, Member_Trainings, Training


@login_required
def index(request):
    member_list = Member.objects.exclude(user__username='admin').order_by('user__last_name')  #
    template = loader.get_template('member_administration/member_overview.html')
    context = {
        'member_list': member_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def member_detail(request, username):
    try:
        user = User.objects.get(username=username)
        member = Member.objects.get(user=user)
        all_qualifications = Qualification.objects.all()
        all_trainingCategories = TrainingCategory.objects.all()
        member_qualifications = MemberHasQualification.objects.filter(member=member)
        all_trainings = Training.objects.all()
        member_trainings = Member_Trainings.objects.filter(member=member)

        training_list = Member_Trainings.objects.filter(member=member).values_list('training', flat=True)

    except Member.DoesNotExist:
        raise Http404("Mitglied existiert nicht")
    return render(request, 'member_administration/member_detail.html',
                  {'member': member,
                   'member_qualifications': member_qualifications,
                   'all_qualifications': all_qualifications,
                   'all_trainingCategories': all_trainingCategories,
                   'all_trainings': all_trainings,
                   'member_trainings': member_trainings,
                   'training_list': training_list,
                   })
