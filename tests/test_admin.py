from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from task_manager.models import Position


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="Admin",
            password="Admin12345"
        )
        self.client.force_login(self.admin_user)
        self.position = Position.objects.create(name="Developer")
        self.worker = get_user_model().objects.create_user(
            username="Worker",
            password="Worker12345",

        )

    def test_worker_position_listed(self):
        """check if worker position is in display list on admin panel"""
        url = reverse("admin:task_manager_worker_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.worker.position)

    def test_worker_detail_position_listed(self):
        url = reverse("admin:task_manager_worker_change", args=[self.worker.id])
        response = self.client.get(url)

        self.assertContains(response, self.worker.position)
