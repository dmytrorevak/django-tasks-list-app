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
            task_name = form.cleaned_data['name']
            task_description = form.cleaned_data['description']
            task_deadline = form.cleaned_data['deadline']
            task = Task.objects.create(name=task_name,
                                       user=user,
                                       description=task_description,
                                       deadline=task_deadline)
            task.save()
            return redirect('/', permanent=True)
    else:
        form = TaskForm()

    return render(request, 'add-task.html', {'form': form})


def edit_task_view(request, task_id):
    return render(request, 'edit-task.html')
