from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TaskStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class TaskPriority(models.Model):
    name = models.CharField(max_length=50, unique=True)
    level = models.PositiveIntegerField(default=1, help_text="Higher value = higher priority")
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-level']

    def __str__(self):
        return f"{self.name} ({self.level})"


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT, related_name="task_status")
    priority = models.ForeignKey(TaskPriority, on_delete=models.PROTECT, related_name="task_priority")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="created_tasks")
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.status.name}"

    def mark_resolved(self):
        self.is_resolved = True
        self.save()
