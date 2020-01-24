from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import GoalStatus, ScrumyGoals, ScrumyHistory
def index(request):
    goal_name = ScrumyGoals.objects.filter(goal_name='Learn Django')
    return HttpResponse(goal_name)

def scrumygoals(request):
    scrumygoals =  ScrumyGoals.objects.all()
    return HttpResponse(scrumygoals)

