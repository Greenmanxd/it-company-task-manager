from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from task_manager.forms import (
    WorkerCreationForm,
    WorkerPositionUpdateForm,
    TaskForm, WorkerSearchForm,
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
    queryset = Worker.objects.select_related("position")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = WorkerSearchForm(initial={
            "username": username
        })

        return context

    def get_queryset(self):
        queryset = Worker.objects.select_related("position")

        form = WorkerSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


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
    success_url = reverse_lazy("task_manager:worker-list")


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5
    template_name = "task_manager/task_list.html"
    queryset = Task.objects.select_related("task_type")


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "task_manager/task_detail.html"
    queryset = Task.objects.prefetch_related("assignees__position")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")

    def post(self, request, *args, **kwargs):
        super(TaskUpdateView, self).post(request, *args, **kwargs)
        task = Task.objects.get(pk=kwargs["pk"])
        task.modified_by = request.user
        task.save()
        return redirect(reverse_lazy("task_manager:task-list"))


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_manager:task-list")
    template_name = "task_manager/task_confirm_delete.html"


def toggle_status(request, pk):
    status = Task.objects.get(id=pk)
    status.is_completed ^= True
    status.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


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


class PositionListView(generic.ListView):
    model = Position
    template_name = "task_manager/position_list.html"


class PositionCreateView(generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task_manager:position-list")
    template_name = "task_manager/position_form.html"


class PositionUpdateView(generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task_manager:position-list")


class PositionDeleteView(generic.DeleteView):
    model = Position
    success_url = reverse_lazy("task_manager:position-list")
