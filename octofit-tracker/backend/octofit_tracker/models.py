from djongo import models
from bson import ObjectId

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = 'teams'
    def __str__(self):
        return self.name

class User(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')
    class Meta:
        db_table = 'users'
    def __str__(self):
        return self.email

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=50)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    date = models.DateField()
    class Meta:
        db_table = 'activities'
    def __str__(self):
        return f"{self.user.email} - {self.type}"

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for = models.ManyToManyField(Team, related_name='workouts', blank=True)
    class Meta:
        db_table = 'workouts'
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard')
    points = models.PositiveIntegerField(default=0)
    class Meta:
        db_table = 'leaderboard'
    def __str__(self):
        return f"{self.team.name} - {self.points} pts"
