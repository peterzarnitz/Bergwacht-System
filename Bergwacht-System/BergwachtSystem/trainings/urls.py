from __future__ import unicode_literals
from django.conf.urls import url

from . import views

app_name = 'trainings'

urlpatterns = [
    url(r'^$', views.training_overview, name='training_overview'),
    url(r'^liste/$', views.training_list, name='training_list'),
    url(r'^termine/$', views.training_dates, name='training_dates'),
    url(r'^zeitmeldung/(?P<training_event_id>[0-9]+)/$', views.register_time_for_training,
        name='register_time_for_training'),
    url(r'^zeitabmeldung/(?P<training_event_id>[0-9]+)/$', views.deregister_time_for_training,
        name='deregister_time_for_training'),
    url(r'^zeitabmeldung/(?P<training_event_id>[0-9]+)/(?P<username>[a-z]+)/$', views.deregister_user_time_for_training,
        name='deregister_user_time_for_training'),
    url(r'^freischalten/(?P<training_event_id>[0-9]+)/$', views.permit_for_training,
        name='permit_for_training'),
    url(r'^anmeldung/(?P<training_event_id>[0-9]+)/(?P<username>[a-z]+)/$', views.register_for_training,
        name='register_for_training'),
    url(r'^abmeldung/(?P<training_event_id>[0-9]+)/(?P<username>[a-z]+)/$', views.deregister_for_training,
        name='deregister_for_training'),
    url(r'^teilnahmeeintragen/(?P<training_event_id>[0-9]+)/$', views.accept_member_trainings,
        name='accept_member_trainings'),
    url(r'^teilnahmeeintragen/(?P<training_event_id>[0-9]+)/(?P<username>[a-z]+)/$', views.register_member_training,
        name='register_member_training'),
]
