from django.shortcuts import render


# widok funkcyjny
def hello(request):
    return render(
        request,
        'viewsapp/hello.html'
    )


