from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import GoalStatus, ScrumyGoals, ScrumyHistory

def query_filter(request, *args, **kwargs):
    name = ScrumyGoals.objects.filter(goal_name='Learn Django').get()
    return HttpResponse(f"{name}")





def index(request):
    goal_name = ScrumyGoals.objects.filter(goal_name='Learn Django')
    return HttpResponse(goal_name)






def move_goal(request, goal_id):
    goal_id = ScrumyGoals.objects.get(goal_id=goal_id)
    return HttpResponse(goal_id)




















































def scrumygoals(request):
    scrumygoals =  ScrumyGoals.objects.all()
    return HttpResponse(f'{scrumygoals}')