from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from articles.controllers import ListArticles
from articles.models import Article, Category


class LatestArticlesView(View):

    def get(self, request):
        context = ListArticles.filter(request, Article.objects)

        html = render(request, 'articles/list.html', context)

        return HttpResponse(html)


class AuthorArticlesView(View):
    def get(self, request, username=None):
        author = get_object_or_404(User, username=username)

        context = ListArticles.filter(request, author.articles)
        context['page_title'] = author.username + ' articles'

        html = render(request, 'articles/list.html', context)

        return HttpResponse(html)


class CategoryArticlesView(View):
    def get(self, request, slug=None):
        category = get_object_or_404(Category, slug=slug)

        context = ListArticles.filter(request, category.articles)
        context['page_title'] = category.name + ' articles'

        html = render(request, 'articles/list.html', context)

        return HttpResponse(html)
