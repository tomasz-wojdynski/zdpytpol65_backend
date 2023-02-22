from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required

from taskapp.models import Task


@permission_required('taskapp.add_task', raise_exception=True)
def task_create_view(request):
    if request.method == "GET":
        return render(
            request,
            'taskapp/create_task.html'
        )

    if request.method == "POST":
        task = request.POST.get('task')

        if task:
            Task.objects.create(name=task)

        return redirect('taskapp:task-list-view')


def task_list_view(request):

    tasks = Task.objects.all()

    return render(
        request,
        'taskapp/tasks.html',
        context={
            'tasks': tasks,
        }
    )


def task_detail_view(request, task_id):
    task = Task.objects.get(id=task_id)

    return render(
        request,
        'taskapp/task.html',
        context={
            'task': task
        }
    )


def task_update_view(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == "GET":
        return render(
            request,
            'taskapp/update_task.html',
            context={
                'task': task,
            }
        )

    if request.method == "POST":
        new_task = request.POST.get('task')

        if new_task:
            task.name = new_task
            task.save()

        return redirect('taskapp:task-list-view')


def task_delete_view(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == "GET":
        return render(
            request,
            'taskapp/delete_task.html',
            context={
                'task': task,
            }
        )

    if request.method == "POST":
        task.delete()
        return redirect('taskapp:task-list-view')
