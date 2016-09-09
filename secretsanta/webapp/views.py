from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/webapp/login')
def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': None}
    return render(request, 'webapp/index.html', context)


def login(request):
    return render(request, 'webapp/login.html')
