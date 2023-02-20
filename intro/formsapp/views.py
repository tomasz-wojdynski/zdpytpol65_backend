from django.shortcuts import render, redirect

from formsapp.models import Message
from formsapp.forms import MessageForm, MessageModelForm


# Formularz html
def contact1(request):
    if request.method == "GET":
        return render(
            request,
            'formsapp/contact1.html'
        )

    elif request.method == "POST":
        data = request.POST

        name = data.get('name')
        email = data.get('email')
        category = data.get('category')
        title = data.get('title')
        body = data.get('body')

        Message.objects.create(
            name=name,
            email=email,
            category=category,
            title=title,
            body=body,
        )

        return redirect('formsapp:contact1')


# Formularz Django
def contact2(request):
    if request.method == "GET":
        form = MessageForm()  # unbound form

        return render(
            request,
            'formsapp/contact2.html',
            context={
                'form': form,
            }
        )

    elif request.method == "POST":
        form = MessageForm(request.POST)  # bound form

        if form.is_valid():
            data = form.cleaned_data

            Message.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                category=data.get('category'),
                title=data.get('title'),
                body=data.get('body')
            )

            return redirect('formsapp:contact2')
        else:

            return render(
                request,
                'formsapp/contact2.html',
                context={
                    'form': form
                }
            )


# Formularz modelu Django
def contact3(request):
    if request.method == "GET":
        form = MessageModelForm()  # unbound form

        return render(
            request,
            'formsapp/contact3.html',
            context={
                'form': form
            }
        )

    elif request.method == "POST":
        form = MessageModelForm(request.POST)  # bound form

        if form.is_valid():
            form.save()

            return redirect('formsapp:contact2')

        else:
            return render(
                request,
                'formsapp/contact3.html',
                context={
                    'form': form,
                }
            )
