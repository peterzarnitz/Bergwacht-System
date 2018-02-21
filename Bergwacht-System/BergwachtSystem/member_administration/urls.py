from django.conf.urls import url

from . import views

app_name = 'member_administration'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<username>[a-z]+)/$', views.member_detail, name='member_detail'),
]