from datetime import datetime

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from articles.models import Article, Comment

DEFAULT_COMMENTS_SHOWN = 10

class ArticleDetailView(View):

    def get(self, request, username, slug):
        comments_page = request.GET.get('page')
        comments_shown = request.GET.get('shown', DEFAULT_COMMENTS_SHOWN)
        shown_param = '&shown={0}'.format(comments_shown) if comments_shown != DEFAULT_COMMENTS_SHOWN else ''
        article = get_object_or_404(Article.objects.select_related('author'), Q(slug=slug) & Q(publication_date__lte=datetime.now()) & Q(state__exact='PB'))

        comments_list = Comment.objects.select_related('article').all().filter(article=article.pk).order_by('-creation_date')

        paginator = Paginator(comments_list, comments_shown)

        comments = paginator.get_page(comments_page)

        context = {'article': article,
                   'username': username,
                   'comments': comments,
                   'shown_param': shown_param,
                   }

        html = render(request, 'articles/detail.html', context)

        return HttpResponse(html)
