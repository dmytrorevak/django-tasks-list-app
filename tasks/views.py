from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


@login_required
def user_page_view(request):
    user = request.user
    tasks = Task.objects.filter(user_id=user.id)
    return render(request, 'user-page.html', {'tasks': tasks})


def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/', permanent=True)
    else:
        form = SignUpForm()
    return render(request, 'registration/sign-up.html', {'form': form})


@login_required
def add_task_view(request):
    user = request.user
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.save()
            return redirect('/', permanent=True)
    else:
        form = TaskForm()
    return render(request, 'add-task.html', {'form': form})


@login_required
def edit_task_view(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        form.save()
        return redirect('/', permanent=True)
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit-task.html', {'form': form, 'task': task})


def remove_task_view(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('/', permanent=True)
