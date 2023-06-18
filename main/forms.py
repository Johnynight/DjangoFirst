from django.forms import forms, ModelForm
from .models import Post, Comments


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'draft']


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'body']
