from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('tofunmiscrumy/', views.index),
    path('scrumygoals/', views.scrumygoals),
    path('query_filter', views.query_filter),
]


