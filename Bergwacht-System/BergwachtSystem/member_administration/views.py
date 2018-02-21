# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render

from .models import Member, User, Qualification, MemberHasQualification


@login_required
def index(request):
    member_list = Member.objects.filter(user__is_superuser='False').order_by('user__last_name')  #
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
        member_qualifications = MemberHasQualification.objects.filter(member=member)
    except Member.DoesNotExist:
        raise Http404("Mitglied existiert nicht")
    return render(request, 'member_administration/member_detail.html',
                  {'member': member, 'member_qualifications': member_qualifications, 'all_qualifications': all_qualifications})
