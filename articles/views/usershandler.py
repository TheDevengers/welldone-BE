from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from articles.controllers import UsersList

class UserListView(View):

    def get(self, request):
        page = request.GET.get('page', 1)
        shown = request.GET.get('shown', 10)

        users_list, query_params = UsersList.filter(search_name=search,
                                                    page=page,
                                                    shown=shown)

        context = dict(
            users=users_list,
            query_params=query_params
        )
        return HttpResponse(render(request, 'articles/users.html', context))

    def post(self, request):
        pass
