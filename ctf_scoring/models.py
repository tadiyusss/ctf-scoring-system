from django.db import models
from django.contrib.auth.models import User

class Level(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Question(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question
    

class Solved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    ip_address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)
    ip_address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flag = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now=True)
    ip_address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username