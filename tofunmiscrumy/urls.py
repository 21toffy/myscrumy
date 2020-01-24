from django.contrib import admin
from django.urls import path

from . import views


app_name='tofunmiscrumy'

urlpatterns = [
    path('tofunmiscrumy/', views.index),
    path('scrumygoals/', views.scrumygoals),
    path('query_filter', views.query_filter),
    path('tofunmiscrumy/movegoal/<int:goal_id>', views.move_goal),
]


