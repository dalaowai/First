from django.shortcuts import render
from .forms import CustomerForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def  singin(request):

    form = CustomerForm()
    
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            
    return render(request, 'main/singin.html', {'form':form})