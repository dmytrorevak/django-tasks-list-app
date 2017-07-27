from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *


@login_required
def user_page_view(request):
    user = request.user
    tasks = Task.objects.filter(user_id=user.id)
    return render(request, 'user-page.html', {'tasks': tasks})
