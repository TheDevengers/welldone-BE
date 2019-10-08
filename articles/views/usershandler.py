from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User

class UserListView(View):

    def get(self, request):
        users = User.objects.all()
        context = dict(
            users=users
        )
        return HttpResponse(render(request, 'articles/users.html', context))