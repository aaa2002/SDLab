from django.db import models
from enum import Enum

class Role(Enum):
    USER = 'user'
    ADMIN = 'admin'

class User(models.Model):
    name = models.CharField(max_length=255) 
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=[(role.value, role.name) for role in Role])

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'server'

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'server'

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'server'

class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'server'

class Document(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'server'

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.user} on {self.document}"

    class Meta:
        app_label = 'server'

class TimeTrack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user} tracked time on {self.task}"

    class Meta:
        app_label = 'server'
