from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'main/index.html')


@login_required(login_url='login')
def about(request):
    return render(request, 'main/about.html')

  