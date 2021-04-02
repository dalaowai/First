from django.shortcuts import render
from .forms import CustomerForm
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def singin(request):

    if request.method == 'POST':
        email = request.POST.get("email")
        return HttpResponse("<h2>Опять ты, {0}</h2>".format(email))

    else:
        form = CustomerForm()
        return render(request, 'main/singin.html', {'form': form})