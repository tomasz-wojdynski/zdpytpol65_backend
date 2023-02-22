from django import views
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView

from django.contrib.auth.decorators import login_required

from viewsapp.models import Person

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


# Coś z CRUDa
# R - Read (widok detalu)

# Widok funkcyjny
@login_required(login_url='authapp:login')
def person_detail(request, person_id):
    #person = Person.objects.get(id=person_id)
    person = get_object_or_404(Person, id=person_id)

    return render(
        request,
        'viewsapp/person_detail.html',
        context={
            'person': person
        }
    )


# Widok klasowy
class PersonView(views.View):
    def get(self, request, person_id):
        person = get_object_or_404(Person, id=person_id)

        return render(
            request,
            'viewsapp/person_detail.html',
            context={
                'person': person
            }
        )


# Widok generyczny
class PersonDetailView(DetailView):
    model = Person
