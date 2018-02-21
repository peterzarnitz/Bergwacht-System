from django.conf.urls import url

from . import views

app_name = 'trainings'

urlpatterns = [
    url(r'^$', views.training_overview, name='training_overview'),
]
