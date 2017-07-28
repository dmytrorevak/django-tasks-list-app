from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
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
