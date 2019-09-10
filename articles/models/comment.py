from django.db import models
from django.contrib.auth.models import User
from .article import Article

class Comment(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    text = models.TextField(max_length=500, verbose_name='Comment body')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Comment author')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Article')
    creation_date = models.DateField(verbose_name='Creation date', auto_now_add=True)

    def __str__(self):
        return self.title