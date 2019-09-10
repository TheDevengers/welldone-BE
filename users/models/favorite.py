from django.db import models
from django.contrib.auth.models import User
from articles.models import Article

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.article_id.title