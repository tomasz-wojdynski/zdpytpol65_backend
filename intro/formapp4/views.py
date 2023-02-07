# Formularz post - dane zapisywane do pamięci trwałej (baza)
from django.shortcuts import render, redirect

from formapp4.models import Task

def register(request):
    if request.method == "GET":
        # Wczytywanie z bazy
        tasks = Task.objects.all()

        return render(
            request,
            'formapp4/register.html',
            context={
                'tasks': tasks,
            }
        )

    elif request.method == "POST":
        task = request.POST.get('task')

        # Zapisywanie do bazy
        if task:
            t = Task(name=task)
            t.save()

        return redirect('formapp4:register')
