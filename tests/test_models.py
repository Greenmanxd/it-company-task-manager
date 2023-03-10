import datetime

from django.test import TestCase

from task_manager.models import Position, TaskType, Worker, Task


class ModelTest(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="Developer")
        self.task_type = TaskType.objects.create(name="New Feature")
        self.worker = Worker.objects.create_user(
            username="Test",
            first_name="test name",
            last_name="test last name",
            password="Test12345",
        )

    def test_position_str(self):
        self.assertEqual(str(self.position), self.position.name)

    def test_task_type_str(self):
        self.assertEqual(str(self.task_type), self.task_type.name)

    def test_worker_str(self):
        if self.worker.first_name and self.worker.last_name:
            self.assertEqual(
                str(self.worker),
                f"{self.worker.username} ({self.worker.first_name} {self.worker.last_name}) {self.worker.position}"
            )
        else:
            self.assertEqual(str(self.worker), f"{self.worker.username} {self.worker.position}")

    def test_task_str(self):
        self.task = Task.objects.create(
            name="test",
            description="test description",
            created_by=self.worker,
            task_type=self.task_type,
            deadline=datetime.datetime.now()
        )
        self.assertEqual(str(self.task), f"{self.task.name}: {self.task.description}")

