# Formularz post - dane zapisywane do pamięci trwałej (plik)
from django.shortcuts import render, redirect


def register(request):
    if request.method == "GET":
        # Wczytywanie z pliku
        with open('tasks.txt', 'r') as f:
            tasks = f.readlines()

        return render(
            request,
            'formapp3/register.html',
            context={
                'tasks': tasks,
            }
        )

    elif request.method == "POST":
        task = request.POST.get('task')

        # Zapisywanie do pliku
        if task:
            with open('tasks.txt', 'a') as f:
                f.write(task + "\n")

        return redirect('formapp3:register')
