# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Member, Qualification, MemberHasQualification


class ProfileInline(admin.StackedInline):
    model = Member
    can_delete = False
    verbose_name_plural = 'Mitglied'

class MemberUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(MemberUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, MemberUserAdmin)
admin.site.register(Qualification)
admin.site.register(MemberHasQualification)