from django.http import HttpResponse
from django.views import View


class ArticleDetailView(View):
    def get(self, request):
        # TODO Implementar vista
        return HttpResponse()
