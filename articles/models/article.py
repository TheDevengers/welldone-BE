from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from .category import Category

DRAFT = 'DR'
PUBLISHED = 'PB'

ART_STATE = {
    (DRAFT, 'Draft'),
    (PUBLISHED, 'Published'),
}


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author', related_name='articles')
    introduction = models.TextField(max_length=250, verbose_name='Introduction')
    body = models.TextField(max_length=2000, verbose_name='Body')
    categories = models.ManyToManyField(Category, verbose_name='Categories')
    response_to = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Response to')
    state = models.CharField(max_length=2, verbose_name='Article state', choices=ART_STATE, default=DRAFT)
    slug = models.SlugField()
    image = models.ImageField(verbose_name='Image noted')
    publication_date = models.DateTimeField(verbose_name='Publication date', default=datetime.now)
    creation_date = models.DateTimeField(verbose_name='Creation date', auto_now_add=True)
    modification_date = models.DateTimeField(verbose_name='Modification date', auto_now=True)

    def __str__(self):
        return self.title
