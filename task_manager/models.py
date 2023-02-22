from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


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
        if self.first_name and self.last_name:
            return f"{self.username} ({self.first_name} {self.last_name}) {self.position}"
        return f"{self.username} {self.position}"

    def get_absolute_url(self):
        return reverse("task_manager:worker-detail", kwargs={"pk": self.pk})


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField(max_length=12)
    is_completed = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(Worker, on_delete=models.CASCADE)
    modified_on = models.DateField(auto_now=True, blank=True, null=True)
    modified_by = models.ForeignKey(
        Worker,
        on_delete=models.DO_NOTHING,
        related_name="Project_modified_by",
        null=True,
        blank=True
    )

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
