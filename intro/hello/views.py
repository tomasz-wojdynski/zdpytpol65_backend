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

