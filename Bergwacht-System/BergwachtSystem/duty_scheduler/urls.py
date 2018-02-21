from django.conf.urls import url

from . import views

app_name = 'duty_scheduler'

urlpatterns = [
    url(r'^$', views.duty_list, name='duty_list'),
    url(r'^calendar/$', views.duty_calendar, name='duty_calendar'),
    url(r'^(?P<duty_number>[0-9]+)/$', views.duty_detail, name='duty_detail'),
    url(r'^anmeldung/(?P<duty_number>[0-9]+)/$', views.duty_signin, name='duty_signin'),
    url(r'^abmeldung/(?P<duty_number>[0-9]+)/$', views.duty_signout, name='duty_signout'),
]
