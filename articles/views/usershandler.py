from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User

class UserListView(View):

    def get(self, request):
        search = request.GET.get('search-name')
        if search:
            users = User.objects.filter(username__icontains=search).order_by('username')
        else:
            users = User.objects.all().order_by('username')
        context = dict(
            users=users
        )
        return HttpResponse(render(request, 'articles/users.html', context))

    def post(self, request):
        pass
