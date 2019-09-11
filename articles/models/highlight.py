from django.db import models
from .article import Article
from django.contrib.auth.models import User

class Highlight(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=200, verbose_name='Highlighted text')

    def __str__(self):
        return self.text