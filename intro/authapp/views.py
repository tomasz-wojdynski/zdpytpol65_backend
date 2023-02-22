from django.shortcuts import render


# Create your views here.
def home(request):
    # print(request.user)

    return render(
        request,
        'authapp/home.html',
    )


def login_view(request):
    return render(
        request,
        'authapp/login.html',
    )