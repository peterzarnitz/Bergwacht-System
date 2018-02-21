# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import Duty_signup_form
from .models import Duty, Member, Takes_part_in_duty


@login_required
def duty_list(request):
    duty_list = Duty.objects.order_by('duty_start', 'duty_area')
    return render(request, 'duty_scheduler/duty_list.html',
                  {'duty_list': duty_list, 'current_member': Member.objects.get(user=request.user)})


@login_required
def duty_detail(request, duty_number):
    try:
        duty = Duty.objects.get(duty_number=duty_number)
        duty.members.order_by('-status', 'user__last_name')
    except Duty.DoesNotExist:
        raise Http404("Dienst existiert nicht")
    return render(request, 'duty_scheduler/duty_detail.html', {'duty': duty})


@login_required
def duty_calendar(request):
    duty_list = Duty.objects.all()
    return render(request, 'duty_scheduler/duty_calendar.html',
                  {'duty_list': duty_list, 'current_member': Member.objects.get(user=request.user)})


@login_required
def duty_signin(request, duty_number):
    try:
        duty = Duty.objects.get(duty_number=duty_number)
    except Duty.DoesNotExist:
        raise Http404("Dienst existiert nicht")

    error_message = ''
    if request.method == "POST":
        form = Duty_signup_form(request.POST)
        if form.is_valid():
            signup = form.save(commit=False)
            signup.member = Member.objects.get(user=request.user)
            signup.duty = duty
            if signup.from_time < signup.to_time and signup.member != duty.members.all:
                if signup.from_time >= duty.duty_start or signup.to_time <= duty.duty_end:
                    signup.save()
                    return redirect('duty_scheduler:duty_detail', duty_number=duty_number)
                else:
                    error_message = 'Anmeldezeitraum muss innerhalb des Dienstzeitraums liegen'
            else:
                error_message = 'Abmeldezeit muss nach Anmeldezeit liegen'

    else:
        form = Duty_signup_form()
    return render(request, 'duty_scheduler/duty_register.html',
                  {'form': form, 'duty': duty, 'error_message': error_message})


@login_required
def duty_signout(request, duty_number):
    user = request.user
    member = Member.objects.get(user=user)
    duty = Duty.objects.get(duty_number=duty_number)
    Takes_part_in_duty.objects.get(duty=duty, member=member).delete()
    return duty_list(request)
