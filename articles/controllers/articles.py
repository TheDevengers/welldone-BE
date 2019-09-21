from datetime import datetime

from django.core.paginator import Paginator

DEFAULT_SHOWN = 10


class ListArticles(object):

    @staticmethod
    def filter(request, article_objects):
        page = request.GET.get('page')
        shown = request.GET.get('shown', DEFAULT_SHOWN)
        shown_param = '&shown={0}'.format(shown) if shown != DEFAULT_SHOWN else ''

        article_list = article_objects.select_related('author').all()\
            .filter(publication_date__lte=datetime.now(), state__exact='PB')\
            .order_by('-publication_date')
        paginator = Paginator(article_list, shown)

        articles = paginator.get_page(page)

        context = {
            'article_list': articles,
            'shown_param': shown_param,
            'page_title': 'Latest articles',
        }

        return context
