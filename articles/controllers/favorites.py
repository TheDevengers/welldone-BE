from django.shortcuts import get_object_or_404

from articles.models import Article, Favorite

class FavoriteController(object):

    @staticmethod
    def add_favorite(user, slug):
        favorite = Favorite()
        favorite.user = user
        article = get_object_or_404(Article, slug=slug)
        favorite.article = article
        favorite.save()