from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('tofunmiscrumy/', views.index),
    path('scrumygoals/', views.scrumygoals),
]


