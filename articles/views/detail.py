from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from articles.models import Article, Comment


class ArticleDetailView(View):

    def get(self, request, username, slug):

        article = get_object_or_404(Article.objects.select_related('author'), Q(slug=slug) & Q(publication_date__lte=datetime.now()) & Q(state__exact='PB'))

        comments = Comment.objects.select_related('article').all().filter(article=article.pk)

        context = {'article': article,
                   'username': username,
                   'comments': comments}

        html = render(request, 'articles/detail.html', context)

        return HttpResponse(html)
