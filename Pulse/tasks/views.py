from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, TaskStatus
from .forms import TaskForm
from django.views.decorators.http import require_POST


def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm()
    return render(request, 'tasks/tasks.html', {'tasks': tasks, 'form': form})

def task_table(request):
    tasks = Task.objects.all()
    form = TaskForm()
    return render(request, 'tasks/tasks_table.html', {'tasks': tasks, 'form': form})

def task_kanban(request):
    """
    Render tasks in a Kanban board grouped by status.
    """
    statuses = TaskStatus.objects.all()
    status_tasks = {status: Task.objects.filter(status=status) for status in statuses}
    return render(request, "tasks/tasks_kanban.html", {"status_tasks": status_tasks})

def task_gantt(request):
    tasks = Task.objects.all()
    form = TaskForm()
    return render(request, 'tasks/tasks_gantt.html', {'tasks': tasks, 'form': form})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    return redirect('task_list')

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/tasks.html', {'task': task})

@require_POST
def task_resolve(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.mark_resolved()  # uses your model's method
    return redirect('task_list')
