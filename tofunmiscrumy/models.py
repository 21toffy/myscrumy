from django.db import models
from django.contrib.auth.models import User 

class GoalStatus(models.Model):
    status_name = models.CharField(max_length=50)

class ScrumyGoal(models.Model):
    goal_name = models.CharField(max_length=50) 
    goal_id = models.IntegerField ()
    created_by = models.CharField(max_length=50)
    moved_by = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    goal_status = models.ForeignKey(GoalStatus, on_delete = models.PROTECT)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="user_goal")
    
class ScrumyHistory(models.Model):
    created_by = models.CharField(max_length=50)
    moved_by = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    goal = models.ForeignKey(ScrumyGoal, on_delete=models.CASCADE)


