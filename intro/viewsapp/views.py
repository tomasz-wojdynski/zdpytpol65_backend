from django import views
from django.shortcuts import render


# widok funkcyjny
def hello(request):
    return render(
        request,
        'viewsapp/hello.html'
    )


# widok klasowy
class HelloView(views.View):
    def get(self, request):
        return render(
            request,
            'viewsapp/hello.html'
        )
