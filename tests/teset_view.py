import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from django.urls import reverse

from task_manager.models import Position, Task, TaskType, Worker

WORKER_URL = reverse("task_manager:worker-list")
TASK_URL = reverse("task_manager:task-list")
TASK_TYPE_URL = reverse("task_manager:task-type-list")
POSITION_URL = reverse("task_manager:position-list")


class PublicWorkerTest(TestCase):
    def test_login_require_redirect_worker(self):
        response = self.client.get(WORKER_URL)
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(
            response,
            expected_url="/accounts/login/?next=/worker/"
        )


class PrivateWorkerTest(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="Developer")
        self.user = get_user_model().objects.create_user(
            username="Test",
            password="Test1234"
        )
        self.client.force_login(self.user)

    def test_create_worker(self):
        form_data = {
            "username": "new_user1",
            "password1": "User1234test1",
            "password2": "User1234test1",
            "first_name": "Test first1",
            "last_name": "Test last1",
            "position": 1
        }

        self.client.post(reverse("task_manager:worker-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.position_id, form_data["position"])


class PublicTaskTest(TestCase):
    def test_login_require_redirect_task(self):
        response = self.client.get(TASK_URL)

        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(
            response,
            expected_url="/accounts/login/?next=/task/"
        )


class PrivateTaskTest(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="Developer")

        self.user = get_user_model().objects.create(
            username="test",
            password="Test12345"
        )
        self.client.force_login(self.user)
        self.task_type = TaskType.objects.create(name="Bug")

    def test_retrieve_task(self):
        Task.objects.create(
            name="test",
            description="test",
            deadline=datetime.datetime.now(),
            created_by=self.user,
            task_type=self.task_type,

        )
        Task.objects.create(
            name="test1",
            description="test1",
            deadline=datetime.datetime.now(),
            created_by=self.user,
            task_type=self.task_type,
        )

        response = self.client.get(TASK_URL)
        tasks = Task.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_list"]),
            list(tasks)
        )
        self.assertTemplateUsed(response, "task_manager/task_list.html")


class PublicPositionTest(TestCase):
    def test_login_require_redirect_position(self):
        response = self.client.get(POSITION_URL)

        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(
            response,
            expected_url="/accounts/login/?next=/position/"
        )


class PrivatePositionTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="Test12345"
        )
        self.client.force_login(self.user)

    def test_retrieve_position(self):
        Position.objects.create(name="Developer")
        Position.objects.create(name="QA")

        response = self.client.get(POSITION_URL)
        positions = Position.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["position_list"]),
            list(positions)
        )
        self.assertTemplateUsed(response, "task_manager/position_list.html")


class PublicTaskTypeTest(TestCase):
    def test_login_require_redirect_task_type(self):
        response = self.client.get(TASK_TYPE_URL)

        self.assertNotEqual(response, 200)
        self.assertRedirects(
            response,
            expected_url="/accounts/login/?next=/task-type/"
        )


class PrivateTaskTypeTest(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="Developer")
        self.user = get_user_model().objects.create_user(
            username="test",
            password="Test12345"
        )
        self.client.force_login(self.user)

    def test_retrieve_task_type(self):
        TaskType.objects.create(name="Bug")
        TaskType.objects.create(name="QA")

        response = self.client.get(TASK_TYPE_URL)
        positions = TaskType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["tasktype_list"]),
            list(positions)
        )
        self.assertTemplateUsed(response, "task_manager/task_type_list.html")
