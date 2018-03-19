# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from member_administration.models import Member
from trainings.models import Training, TrainingEvent, Possible_participates_in_trainingevent, \
    Participates_in_trainingevent


@login_required
def training_overview(request):
    return render(request, 'trainings/training_start.html', {'nav': 'start'})


@login_required
def training_list(request):
    training_list = Training.objects.order_by('name')
    return render(request, 'trainings/training_list.html',
                  {'training_list': training_list, 'current_member': Member.objects.get(user=request.user),
                   'nav': 'list'})


@login_required
def training_dates(request):
    training_events = TrainingEvent.objects.order_by('event_start')
    return render(request, 'trainings/training_dates.html',
                  {'training_events': training_events, 'current_member': Member.objects.get(user=request.user),
                   'nav': 'dates'})


@login_required
def register_time_for_training(request, training_event_id):
    currentMember = Member.objects.get(user=request.user)
    training_event = TrainingEvent.objects.get(training_event_id=training_event_id)
    Possible_participates_in_trainingevent.objects.create(
        member=currentMember,
        trainingevent=training_event,
        first_register_timestamp = timezone.now()
    )
    return redirect('/ausbildung/termine/')


@login_required
def deregister_time_for_training(request, training_event_id):
    member = Member.objects.get(user=request.user)
    training_event = TrainingEvent.objects.get(training_event_id=training_event_id)
    Possible_participates_in_trainingevent.objects.filter(member=member, trainingevent=training_event).delete()
    return redirect('/ausbildung/termine/')


@login_required
@user_passes_test(lambda u: u.has_perm('trainings.can_delete_possible_participates_in_trainingevent'))
def deregister_user_time_for_training(request, training_event_id, username):
    user = User.objects.get(username=username)
    member = Member.objects.get(user=user)
    training_event = TrainingEvent.objects.get(training_event_id=training_event_id)
    Possible_participates_in_trainingevent.objects.filter(member=member, trainingevent=training_event).delete()
    return redirect('/ausbildung/freischalten/' + str(training_event_id) + '/')


@login_required
@user_passes_test(lambda u: u.has_perm('trainings.can_add_participates_in_trainingevent'))
def register_for_training(request, training_event_id, username):
    user = User.objects.get(username=username)
    member = Member.objects.get(user=user)
    training_event = TrainingEvent.objects.get(training_event_id=training_event_id)

    possible_participates_in_trainingevent = Possible_participates_in_trainingevent.objects.get(member=member, trainingevent=training_event)

    Participates_in_trainingevent.objects.create(
        member=member,
        trainingevent=training_event,
        first_register_timestamp=possible_participates_in_trainingevent.first_register_timestamp
    )
    possible_participates_in_trainingevent.delete()
    return redirect('/ausbildung/freischalten/' + str(training_event_id) + '/')


@login_required
@user_passes_test(lambda u: u.has_perm('trainings.can_add_participates_in_trainingevent'))
def deregister_for_training(request, training_event_id, username):
    user = User.objects.get(username=username)
    member = Member.objects.get(user=user)
    training_event = TrainingEvent.objects.get(training_event_id=training_event_id)

    participates_in_trainingevent = Participates_in_trainingevent.objects.get(member=member, trainingevent=training_event)

    Possible_participates_in_trainingevent.objects.create(
        member=member,
        trainingevent=training_event,
        first_register_timestamp=participates_in_trainingevent.first_register_timestamp
    )
    participates_in_trainingevent.delete()
    return redirect('/ausbildung/freischalten/' + str(training_event_id) + '/')


@login_required
@user_passes_test(lambda u: u.has_perm('trainings.can_add_participates_in_trainingevent'))
def permit_for_training(request, training_event_id):
    training_event = TrainingEvent.objects.get(training_event_id=training_event_id)
    possible_participants = Possible_participates_in_trainingevent.objects.filter(trainingevent=training_event)

    return render(request, 'trainings/training_permit.html',
                  {'training_event': training_event, 'nav': 'dates', 'possible_participants': possible_participants})
