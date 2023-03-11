import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Worker, Position, Task, TaskType


class SearchTest(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="Developer")
        self.user = get_user_model().objects.create_user(
            username="Test",
            password="Test12345"
        )
        self.client.force_login(self.user)

    def test_search_worker(self):
        response = self.client.get(
            reverse("task_manager:worker-list") + "?username=Test"
        )

        self.assertEqual(
            list(response.context["worker_list"]),
            list(Worker.objects.filter(username__icontains="Test"))
        )

    def test_search_task(self):
        self.task_type = TaskType.objects.create(name="Bug")
        self.task = Task.objects.create(
            name="test",
            description="test",
            deadline=datetime.datetime.now(),
            created_by=self.user,
            task_type=self.task_type,
        )

        response = self.client.get(
            reverse("task_manager:task-list") + "?name=test"
        )

        self.assertEqual(
            list(response.context["task_list"]),
            list(Task.objects.filter(name__icontains="test"))
        )
