from datetime import datetime

from django.core.paginator import Paginator
from django.db.models import Q

DEFAULT_SHOWN = 10
SEARCH_RESULTS = 20

class ListArticles(object):

    @staticmethod
    def filter(request, article_objects):
        search = request.GET.get('search', '').strip()
        page = request.GET.get('page')
        shown = request.GET.get('shown', DEFAULT_SHOWN)
        shown_param = '&shown={0}'.format(shown) if shown != DEFAULT_SHOWN else ''
        search_param = 'search={0}&'.format(search) if search != '' else ''

        article_list = article_objects.select_related('author').all()\
            .filter(publication_date__lte=datetime.now(), state__exact='PB')\
            .order_by('-publication_date')

        article_list = article_list.filter(Q(title__icontains=search) | Q(introduction__icontains=search) | Q(body__icontains=search))\
            .all()[:SEARCH_RESULTS] if search else article_list

        paginator = Paginator(article_list, shown)

        articles = paginator.get_page(page)

        context = {
            'article_list': articles,
            'shown_param': shown_param,
            'search_param': search_param,
            'page_title': 'Latest articles',
            'search': search,
        }

        return context
