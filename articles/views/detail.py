from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from articles.models import Article


class ArticleDetailView(View):

    def get(self, request, username, slug):

        article = get_object_or_404(Article.objects.select_related('author'), slug=slug)

        context = {'article': article, 'username': username}

        html = render(request, 'articles/detail.html', context)

        return HttpResponse(html)
