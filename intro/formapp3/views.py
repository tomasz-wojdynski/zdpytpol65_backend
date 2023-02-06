from django.shortcuts import render, redirect

TASKS = []


def register(request):
    if request.method == "GET":
        return render(
            request,
            'formapp3/register.html',
            context={
                'tasks': TASKS,
            }
        )

    elif request.method == "POST":
        task = request.POST.get('task')

        if task:
            TASKS.append(task)

        return redirect('formapp3:register')
