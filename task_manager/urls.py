from django.urls import path

from task_manager.views import (
    index,
    WorkerListView,
    TaskListView,
    TaskTypeView,
    WorkerCreateView,
    WorkerDetailView
)

urlpatterns = [
    path("", index, name="index"),

    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("worker/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),

    path("tasks/", TaskListView.as_view(), name="task-list"),

    path("task-types/", TaskTypeView.as_view(), name="task-type-list")
]


app_name = "task_manager"
