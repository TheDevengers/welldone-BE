from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout as django_logout


class Logout(View):

    def get(self, request):
        django_logout(request)
        return redirect('latest_articles')
