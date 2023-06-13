from django.shortcuts import render, redirect

from django.views.generic import DetailView, CreateView, ListView, UpdateView
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User


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
