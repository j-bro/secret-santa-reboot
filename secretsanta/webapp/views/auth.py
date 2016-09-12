from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from webapp.forms import UserForm


def signup_user(request):
    """

    :param request:
    :return:
    """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'webapp/signup.html', {'form': form})


def login_user(request):
    """

    :param request:
    :return:
    """
    if request.user.is_authenticated():
        return redirect('home')

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AuthenticationForm(request, data=request.POST)
        # check whether it's valid:
        if form.is_valid():
            username = password = ''
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    next = request.POST['next']
                    if not next:
                        next = 'home'
                    return redirect(next)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthenticationForm()

    return render(request, 'webapp/login.html', {'form': form})


def logout_user(request):
    """

    :param request:
    :return:
    """
    logout(request)
    return redirect('index')