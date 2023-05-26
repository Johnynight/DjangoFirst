from django.db import models
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()
class Post(models.Model):
    title = models.CharField(max_length=128,verbose_name='Заголовок')
    body = models.TextField(verbose_name='Статься')
    draft = models.BooleanField(default=True)
    changed_at = models.DateTimeField(auto_now=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True, verbose_name='Автор')
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title