from markupsafe import escape

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
    return render(request, 'hello.html')
