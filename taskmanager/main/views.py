from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    descriptions = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Main page', 'descriptions': descriptions})


def about(request):
    return render(request, 'main/about.html')


def add(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is incorrect'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add.html', context)
