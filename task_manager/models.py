from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name}) {self.position}"


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField(max_length=12)
    is_completed = models.BooleanField(default=False)

    PRIORITY_CHOICES = (
        ("HI", "High"),
        ("MED", "Medium"),
        ("LOW", "Low"),
    )

    priority = models.CharField(
        max_length=3,
        choices=PRIORITY_CHOICES,
        default="MED"
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE
    )

    assignees = models.ManyToManyField(Worker, related_name="tasks")

    def __str__(self):
        return f"{self.name}: {self.description}"
