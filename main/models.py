from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=128,verbose_name='Заголовок')
    body = models.TextField(verbose_name='Статься')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title