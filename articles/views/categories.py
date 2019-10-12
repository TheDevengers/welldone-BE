from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from articles.models import Category


class CategoriesListView(View):

    def get(self, request):
        categories = Category.objects.all()
        context = dict(
            categories=categories
        )
        return HttpResponse(render(request, 'articles/categories.html', context))
