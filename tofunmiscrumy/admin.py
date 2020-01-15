from django.contrib import admin
from .models import ScrumyGoals, GoalStatus, ScrumyHistory

admin.site.register (ScrumyGoals)
admin.site.register (GoalStatus)
admin.site.register (ScrumyHistory)