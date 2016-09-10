from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def signup_user(request):
    """

    :param request:
    :return:
    """
    return render(request, 'webapp/signup.html')


def login_user(request):
    """

    :param request:
    :return:
    """
    if request.user.is_authenticated():
        return redirect('home')

    username = password = ''
    if request.method == 'POST':
        username = request.POST['inputUsername']
        password = request.POST['inputPassword']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                next = request.POST['next']
                if not next:
                    next = 'home'
                return redirect(next)

    return render(request, 'webapp/login.html')


def logout_user(request):
    """

    :param request:
    :return:
    """
    logout(request)
    return redirect('index')