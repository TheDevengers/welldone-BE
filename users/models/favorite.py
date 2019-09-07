from django.db import models
from django.contrib.auth.models import User
from articles.models import Article

class Favorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.article_id.title