from django.shortcuts import render


def user_page_view(request):
    return render(request, 'user-page.html')
