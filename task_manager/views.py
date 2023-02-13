from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from task_manager.forms import (
    WorkerCreationForm,
    WorkerPositionUpdateForm,
    TaskForm,
)
from task_manager.models import Task, TaskType, Worker, Position


def index(request):

    num_tasks = Task.objects.count()
    in_proces_tasks = Task.objects.filter(is_completed=False).count()
    num_task_types = TaskType.objects.count()
    num_workers = Worker.objects.count()
    num_positions = Position.objects.count()

    num_visits = request.session.get("num_visits", 1)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_task_types": num_task_types,
        "num_positions": num_positions,
        "num_workers": num_workers,
        "num_tasks": num_tasks,
        "in_proces_tasks": in_proces_tasks,
        "num_visits": num_visits
    }

    return render(request, "task_manager/index.html", context=context)


class WorkerListView(generic.ListView):
    model = Worker
    paginate_by = 5
    template_name = "task_manager/worker_list.html"


class WorkerDetailView(generic.DetailView):
    model = Worker
    template_name = "task_manager/worker_detail.html"


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm


class WorkerPositionUpdateView(generic.UpdateView):
    model = Worker
    form_class = WorkerPositionUpdateForm
    success_url = reverse_lazy("task_manager:worker-list")


class WorkerDeleteView(generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("")


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5
    template_name = "task_manager/task_list.html"


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "task_manager/task_detail.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")


def toggle_status(request, pk):
    status = Task.objects.get(id=pk)
    status.is_completed ^= True
    status.save()
    return redirect(reverse_lazy("task_manager:task-list"))


class TaskTypeView(generic.ListView):
    model = TaskType
    paginate_by = 5
    template_name = "task_manager/task_type_list.html"


class TaskTypeCreateView(generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("task_manager:task-type-list")
    template_name = "task_manager/task_type_form.html"


class TaskTypeUpdateView(generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("task_manager:task-type-list")
    template_name = "task_manager/task_type_form.html"


class TaskTypeDeleteView(generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("task_manager:task-type-list")
    template_name = "task_manager/task_type_confirm_delete.html"
