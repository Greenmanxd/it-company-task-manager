from django.contrib.auth.models import AbstractUser
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    HIGH = "HI"
    MEDIUM = "MED"
    LOW = "LOW"
    PRIORITY_CHOICES = [
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low")
    ]
    priority = models.CharField(
        max_length=3,
        choices=PRIORITY_CHOICES,
        default=MEDIUM
    )
    # task_type = models.OneToOneField()


class Worker(AbstractUser):
    pass
