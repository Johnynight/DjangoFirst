from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic import DetailView, CreateView, ListView, UpdateView
from rest_framework import status

from .models import Post, Comments
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer, PostDetailSerializer
from rest_framework.decorators import APIView
from django.views.decorators.http import require_POST


# def home(request):
#     posts = Post.objects.all().order_by('created_at')
#     return render(request, 'main/home.html', {'posts': posts})
#
#
# def post_detail(request, id):
#     try:
#         post = Post.objects.get(id=id)
#     except Post.DoesNotExist:
#         pass
#     return render(request, 'main/post_detail.html', {'post': post})
#
#
# def second_view(request):
#     return render(request, 'main/second.html')
#
#
# def base_view(request):
#     return render(request, 'main/base.html')
#
#
# def post_create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             cd = form.save(commit=False)
#             cd.author = request.user
#             cd.save()
#             return redirect(home)
#     else:
#         form = PostForm()
#     return render(request, 'main/post_create.html', {'form': form})

class PostList(ListView):
    model = Post
    template_name = 'main/home.html'
    context_object_name = 'posts'
    ordering = '-created_at'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['admin_user'] = User.objects.get(id=1)
        if 'counter' in self.request.session:
            self.request.session['counter'] += 1
        else:
            self.request.session['counter'] = 1
        return context

    # def render_to_response(self, context, **response_kwargs):
    #     response = super().render_to_response(context, **response_kwargs)
    #     if 'counter' in self.request.COOKIES:
    #         cnt = int(self.request.COOKIES.get('counter')) + 1
    #         response.set_cookie('counter', cnt)
    #     else:
    #         response.set_cookie('counter', 1)
    #     return response


class PostDetail(DetailView):
    model = Post
    comments = Comments
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = CommentForm()
        post_id = self.kwargs['pk']
        context['comments'] = Comments.objects.filter(post = post_id)
        return context


class PostCreate(CreateView):
    form_class = PostForm
    template_name = 'main/post_create.html'
    success_url = '/blog/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/'


@api_view(['GET'])
def api_detail_posts(request, pk):
    if request.method == 'GET':
        posts = Post.objects.get(pk=pk)
        serializer = PostDetailSerializer(posts)
        return Response(serializer.data)


# @api_view(['GET'])
# def api_posts(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)


class APIpost(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post,
                             id=post_id,
                             status=Post.Status.PUBLISHED)

    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'main/comment.html',
                  {'post': post,
                   'form': form,
                   'comment': comment})
