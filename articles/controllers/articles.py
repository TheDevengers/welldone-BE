from datetime import datetime

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404

from articles.models import Article, Category
from articles.forms import ArticleForm

DEFAULT_SHOWN = 10
SEARCH_RESULTS = 20
DATE_ORDER = {
    'date': '',
    '-date': '-'
}


class ListArticles(object):

    @staticmethod
    def filter(request, article_objects):
        date_order = request.GET.get('order') if request.GET.get('order') and request.GET.get('order') in DATE_ORDER else '-date'
        search = request.GET.get('search', '').strip()
        page = request.GET.get('page')
        shown = request.GET.get('shown', DEFAULT_SHOWN)
        query_params = None
        query_params = query_params + '&shown={0}'.format(shown) if shown != DEFAULT_SHOWN else ''
        query_params = query_params + '&search={0}'.format(search) if search != '' else ''
        query_params = query_params + '&order={0}'.format(date_order) if date_order != '' else ''

        article_list = article_objects.select_related('author').all()\
            .filter(publication_date__lte=datetime.now(), state__exact='PB')\
            .order_by(DATE_ORDER[date_order] + 'publication_date')

        article_list = article_list.filter(Q(title__icontains=search) | Q(introduction__icontains=search) | Q(body__icontains=search))\
            .all()[:SEARCH_RESULTS] if search else article_list

        paginator = Paginator(article_list, shown)

        articles = paginator.get_page(page)

        context = {
            'article_list': articles,
            'query_params': query_params,
            'page_title': 'Latest articles',
            'search': search,
        }

        return context


class CreateArticle(object):

    @staticmethod
    def create_new_article(user, values, slug):
        article = Article()
        article.author = user
        article.response_to = get_object_or_404(Article, slug=slug)
        form = ArticleForm(values, instance=article)
        if form.is_valid():
            form.save()
            categories_selected = form.cleaned_data['categories']
            categories = []
            for category_selected in categories_selected:
                obj = Category.objects.get(id=category_selected.id)
                categories.append(obj)
            article.categories.add(*categories)
            form.save()
            return None
        else:
            return form

