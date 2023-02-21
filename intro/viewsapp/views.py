from django import views
from django.shortcuts import render
from django.views.generic import TemplateView


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


# Widok generyczny
class HelloTemplateView(TemplateView):
    template_name = 'viewsapp/hello.html'
