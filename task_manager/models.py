from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=255)


class Position(models.Model):
    name = models.CharField(max_length=255)


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)

    HIGH = "HI"
    MEDIUM = "MED"
    LOW = "LOW"

    PRIORITY_CHOICES = (
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low")
    )

    priority = models.CharField(
        max_length=3,
        choices=PRIORITY_CHOICES,
        default=MEDIUM
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE
    )

    assignees = models.ManyToManyField(Worker, related_name="tasks")
