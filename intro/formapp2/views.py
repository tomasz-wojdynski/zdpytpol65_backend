from django.shortcuts import render, redirect

TASKS = []


# Version II
def register(request):
    if request.method == "GET":
        return render(
            request,
            'formapp2/register.html',
            context={
                'tasks': TASKS,
            }
        )

    elif request.method == "POST":
        task = request.POST.get('task')

        if task:
            TASKS.append(task)

        return redirect('formapp2:register')
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

