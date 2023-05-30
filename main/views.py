from django.shortcuts import render

from .models import Post



def home(request):
    posts = Post.objects.all().order_by('created_at')
    return render(request, 'main/home.html', {'posts': posts})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'main/post_detail.html', {'post': post})

def second_view(request):
    return render(request, 'main/second.html')


def base_view(request):
    return render(request, 'main/base.html')
