from django.urls import path

from task_manager.views import (
    index,
    WorkerListView,
    TaskListView,
    TaskTypeView,
    WorkerCreateView,
    WorkerDetailView,
    WorkerPositionUpdateView,
    WorkerDeleteView,
    TaskDetailView,
    TaskUpdateView,
    TaskCreateView
)

urlpatterns = [
    path("", index, name="index"),

    path("worker/", WorkerListView.as_view(), name="worker-list"),
    path("worker/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("worker/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("worker/<int:pk>/update", WorkerPositionUpdateView.as_view(), name="worker-update"),
    path("worker/<int:pk>/delete", WorkerDeleteView.as_view(), name="worker-delete"),

    path("task/", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),

    path("task-type/", TaskTypeView.as_view(), name="task-type-list")
]


app_name = "task_manager"
