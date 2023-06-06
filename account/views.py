from django.shortcuts import render

from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_view(request):
    logout(request)
    return redirect('home')  # Замените 'home' на URL-шаблон вашей домашней страницы

# Create your views here.
