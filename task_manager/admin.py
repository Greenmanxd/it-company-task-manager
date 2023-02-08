from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from task_manager.models import Worker, Task, TaskType, Position


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass
