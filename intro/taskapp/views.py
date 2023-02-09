from django.shortcuts import render


def create_task_view(request):
    return render(
        request,
        'taskapp/create_task.html'
    )
