from django.http import HttpResponse
from django.shortcuts import render

from articles.models import Article


def latest_articles(request):
    articles = Article.objects.all()

    context = {'latest_articles': articles}

    html = render(request, 'articles/latest.html', context)

    return HttpResponse(html)
