from django.db import models
from django.contrib.auth.models import User 

class GoalStatus(models.Model):
    status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.status_name

class ScrumyGoals(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT, related_name="user_goal")
    goal_name = models.CharField(max_length=100) 
    goal_id = models.IntegerField ()
    created_by = models.CharField(max_length=100)
    moved_by = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    goal_status = models.ForeignKey(GoalStatus, on_delete = models.PROTECT)
    
    def __str__(self):
        return self.goal_name

class ScrumyHistory(models.Model):
    created_by = models.CharField(max_length=50)
    moved_by = models.CharField(max_length=50)
    moved_from = models.CharField(max_length=50)
    moved_to = models.CharField(max_length=50)
    time_of_action = models.DateField()
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.PROTECT)

    def __str__(self):
        return self.created_by



