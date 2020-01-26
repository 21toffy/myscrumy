from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import GoalStatus, ScrumyGoals, ScrumyHistory
from random import randint
from django.shortcuts import render, get_object_or_404, redirect


def query_filter(request, *args, **kwargs):
    name = ScrumyGoals.objects.filter(goal_name='Learn Django').get()
    return HttpResponse(f"{name}")





def index(request):
    goal_name = ScrumyGoals.objects.filter(goal_name='Learn Django')
    return HttpResponse(goal_name)




def move_goal(request, goal_id):
    goal_id = ScrumyGoals.objects.get(goal_id=goal_id)
    return HttpResponse(goal_id)





def add_goal(request):
    goalid=randint(1000,9999)
    goalstatus= GoalStatus.objects.get(status_name='Weekly Goal')
    goal_user = User.objects.get(username='Louis')

    scrumygoals=ScrumyGoals.objects.create(
        goal_name = 'Keep Learning Django',
        goal_id = goalid,
        created_by= 'Louis',
        moved_by = 'Louis',
        owner= 'Louis',
        goal_status=goalstatus,
        user= goal_user,

   )

    scrumygoals.save()
    ret=ScrumyGoals.objects.filter(goal_name = 'keep Learning Django')
    return HttpResponse(ret)




def home(request):
    goal = ScrumyGoals.objects.filter(goal_name='keep Learning Django').first()
    # output = ', '.join([eachgoal.goal_name for eachgoal in goal])
    context={

        'goal':goal,
        'goal_name':goal.goal_name,
        'goal_id':goal.goal_id,
        'user':goal.user,
    }
    return render(request, 'tofunmiscrumy/home.html', context)













































def scrumygoals(request):
    scrumygoals =  ScrumyGoals.objects.all()
    return HttpResponse(f'{scrumygoals}')