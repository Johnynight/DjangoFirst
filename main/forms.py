from django.forms import forms, ModelForm
from .models import Post



class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'draft']
