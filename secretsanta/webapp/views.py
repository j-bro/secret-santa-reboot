from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': None}
    return render(request, 'webapp/index.html', context)


@login_required
def home(request):
    return render(request, 'webapp/home.html')


def signup_user(request):
    return render(request, 'webapp/signup.html')


def login_user(request):
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
    logout(request)
    return redirect('index')