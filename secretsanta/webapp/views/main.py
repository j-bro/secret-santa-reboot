from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': None}
    return render(request, 'webapp/index.html', context)


@login_required
def home(request):
    # return render(request, 'webapp/home.html')
    return redirect('group_list')


def how_it_works(request):
    return render(request, 'webapp/how_it_works.html')
