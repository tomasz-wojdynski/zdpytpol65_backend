from markupsafe import escape
from datetime import datetime

from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse(
        """
        <html>
            <head>
            </head>
            <body>
                <h3 onclick='alert("Hi!");'>Hello, world!</h3>
            </body>
        </html>
        """
    )


def adam(request):
    return HttpResponse("Witaj, Adam!")


def ewa(request):
    return HttpResponse("Witaj, Ewa!")


def hello(request, name):
    print(name)
    safe_name = escape(name)
    print(safe_name)
    return HttpResponse(f"Hello, {safe_name}!")


def greet(request):
    return render(request, 'greet.html')


def hello2(request, name):
    return render(request, 'hello.html', context={'name': name})


def is_monday(request):
    now = datetime.now()
    ans = False
    print(now.weekday())
    if now.weekday() == 2:
        ans = True

    return render(
        request,
        'monday.html',
        context={'is_monday': ans}
    )


class Cow:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def show_fruits(request):
    fruits = [
        'jabłko',
        'banan',
        'winogrona',
        'mandarynki'
    ]
    user = {
        'name': "Jan",
        'surname': "Kowalski",
        "age": 10
    }
    cow_1 = Cow("Mućka", 2)

    return render(
        request,
        'fruits.html',
        context={
            'fruits': fruits,
            'user': user,
            'cow_1': cow_1
        }
    )