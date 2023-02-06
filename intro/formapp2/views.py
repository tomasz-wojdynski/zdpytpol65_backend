# Formularz post - dane zapisywane do pamięci RAM
from django.shortcuts import render, redirect

TASKS = []


# Version II
def register(request):
    if request.method == "GET":
        # Wczytywanie z listy TASKS
        return render(
            request,
            'formapp2/register.html',
            context={
                'tasks': TASKS,
            }
        )

    elif request.method == "POST":
        task = request.POST.get('task')

        # Zapisywanie do listy TASKS
        if task:
            TASKS.append(task)

        return redirect('formapp2:register')
        # return redirect('/form2/')
        # return redirect('/form2/')


# Version I
# def register(request):
#     task = request.POST.get('task')
#
#     if task:
#         TASKS.append(task)
#
#     return render(
#         request,
#         'formapp2/register.html',
#         context={
#             'tasks': TASKS,
#         }
#     )

