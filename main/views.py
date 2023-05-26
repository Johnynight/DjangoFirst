from django.shortcuts import render
from .models import Post
def home(request):
    posts = Post.objects.all()
    return render(request, 'main/home.html',{'posts': posts})


def second_view(request):
    return render(request, 'main/second.html')