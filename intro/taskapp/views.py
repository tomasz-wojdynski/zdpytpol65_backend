from django.shortcuts import render, redirect

from taskapp.models import Task


def create_task_view(request):
    if request.method == "GET":
        return render(
            request,
            'taskapp/create_task.html'
        )

    if request.method == "POST":
        task = request.POST.get('task')

        if task:
            Task.objects.create(name=task)

        return redirect('taskapp:create-task-view')
