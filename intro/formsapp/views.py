from django.shortcuts import render, redirect

from formsapp.models import Message


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
