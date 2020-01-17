# Generated by Django 2.0.13 on 2020-01-17 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GoalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyGoals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_name', models.CharField(max_length=50)),
                ('goal_id', models.IntegerField()),
                ('created_by', models.CharField(max_length=50)),
                ('moved_by', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('goal_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tofunmiscrumy.GoalStatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_goal', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=50)),
                ('moved_by', models.CharField(max_length=50)),
                ('moved_from', models.CharField(max_length=50)),
                ('moved_to', models.CharField(max_length=50)),
                ('time_of_action', models.DateField()),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tofunmiscrumy.ScrumyGoals')),
            ],
        ),
    ]
