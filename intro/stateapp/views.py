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


def set_session(request):

    request.session['counter'] = 0

    return render(
        request,
        'stateapp/session.html'
    )


def show_session(request):
    if 'counter' in request.session:
        request.session['counter'] += 1

    return render(
        request,
        'stateapp/show_session.html',
        context={
            'counter': request.session.get('counter'),
        }
    )


def delete_session(request):
    if 'counter' in request.session:
        del request.session['counter']

    return render(
        request,
        'stateapp/session.html'
    )
