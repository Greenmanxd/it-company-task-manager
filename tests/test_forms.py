from django.test import TestCase

from task_manager.forms import WorkerCreationForm
from task_manager.models import Worker, Position


class CreationFormTest(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="Developer")
        self.user = Worker.objects.create_user(
            username="test_user",
            password="User12345",
        )
        self.client.login(username=self.user.username, password="User12345")

    def test_worker_creation_form(self):
        form_data = {
            "username": "test-user",
            "password1": "Test12345",
            "password2": "Test12345",
            "first_name": "test-first",
            "last_name": "test-last",
            "position": self.position,
            "is_superuser": False,
        }

        form = WorkerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

