from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    # print(request.user)

    return render(
        request,
        'authapp/home.html',
    )


def login_view(request):
    if request.method == "GET":
        return render(
            request,
            'authapp/login.html',
        )

    elif request.method == "POST":
        data = request.POST

        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)  # uwierzytelenienie

        if user:
            login(request, user)  # logowanie (czyli utworzenie uwierzytelnionej sesji)

        return redirect('authapp:home')


def logout_view(request):
    logout(request)
    return redirect('authapp:home')
