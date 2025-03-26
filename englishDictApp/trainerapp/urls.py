from django.contrib import admin
from django.urls import path

from . import views

app_name = 'trainerapp'

urlpatterns = [
    path('', view=views.construct_trainer_page, name='contruct'),
    path('test/', view=views.trainer_page, name='trainer')

]
