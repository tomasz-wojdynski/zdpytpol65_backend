from django.shortcuts import render


# C/U ciasteczek
def set_cookie(request):
    res = render(
        request,
        'stateapp/cookie.html'
    )

    # res.set_cookie('user', 'John', max_age=10)
    res.set_cookie('user', 'Jane')

    return res


# R ciasteczka
def show_cookies(request):
    return render(
        request,
        'stateapp/show_cookies.html',
        context={
            'cookies': request.COOKIES
        }
    )


# D ciasteczka
def delete_cookie(request):
    res = render(
        request,
        'stateapp/cookie.html'
    )

    res.delete_cookie('user')

    return res
