from django.urls import path, include

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
    TaskCreateView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
    TaskDeleteView,
    toggle_status,
    PositionListView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView
)

urlpatterns = [
    path("", index, name="index"),

    path("worker/", WorkerListView.as_view(), name="worker-list"),
    path("worker/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("worker/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("worker/<int:pk>/update/", WorkerPositionUpdateView.as_view(), name="worker-update"),
    path("worker/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),

    path("task/", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/update/complete/", toggle_status, name="toggle_status"),

    path("task-type/", TaskTypeView.as_view(), name="task-type-list"),
    path("task-type/create/", TaskTypeCreateView.as_view(), name="task-type-create"),
    path("task-type/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="task-type-update"),
    path("task-type/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="task-type-delete"),

    path("position/", PositionListView.as_view(), name="position-list"),
    path("position/create/", PositionCreateView.as_view(), name="position-create"),
    path("position/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("position/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),
]


app_name = "task_manager"
