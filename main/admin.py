from django.contrib import admin
from .models import Post, Comments


# admin.site.register(Post)
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'draft']
    list_filter = ['draft', 'author']
    search_fields = ['title', 'body']
    ordering = ['-draft', '-created_at']
    date_hierarchy = 'changed_at'


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'activate']
    list_filter = ['activate', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
