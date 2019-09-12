from datetime import datetime

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from articles.models import Article


class LatestArticlesView(View):
    def get(self, request):
        page = request.GET.get('page')
        shown = request.GET.get('shown', 10)

        article_list = Article.objects.select_related('author').all()\
            .filter(publication_date__lte=datetime.now(), state__exact='PB')\
            .order_by('-publication_date')
        paginator = Paginator(article_list, shown)

        articles = paginator.get_page(page)

        context = {'latest_articles': articles}

        html = render(request, 'articles/latest.html', context)

        return HttpResponse(html)


class ArticleDetailView(View):
    def get(self, request):
        # TODO Implementar vista
        return HttpResponse()
