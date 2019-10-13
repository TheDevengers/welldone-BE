from django.contrib.auth.models import User
from django.core.paginator import Paginator

DEFAULT_SHOWN = 10

class UsersList(object):

    @staticmethod
    def filter(search_name, page=1, shown=DEFAULT_SHOWN):

        if search_name:
            users_list = User.objects.filter(username__icontains=search_name).order_by('username')
        else:
            users_list = User.objects.all().order_by('-date_joined')

        query_params = ''
        query_params = query_params + '&shown={0}'.format(shown) if shown != DEFAULT_SHOWN else ''
        query_params = query_params + '&search={0}'.format(search_name) if search_name is not None else ''

        paginator = Paginator(users_list, shown)

        users_list_page = paginator.get_page(page)

        return users_list_page, query_params
