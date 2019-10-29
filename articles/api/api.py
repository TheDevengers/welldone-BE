from django.db.models import Q
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404

from articles.models import Category, Article, Favorite
from articles.permissions import ArticlePermission, FavoritePermission
from articles.serializers import CategorySerializer, ArticleSerializer, ArticleListSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class ArticlesAPI(ListCreateAPIView):
    permission_classes = [ArticlePermission]

    def get_queryset(self):
        queryset = Article.objects.all()
        return queryset.filter(Q(author=self.request.user))

    def get_serializer_class(self):
        return ArticleListSerializer if self.request.method == 'GET' else ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleAPI(RetrieveUpdateDestroyAPIView):

    queryset = Article.objects.all().select_related('author')
    serializer_class = ArticleSerializer


class CategoriesAPI(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FavoritesAPI(ListCreateAPIView):
    permission_classes = [FavoritePermission]

    def get_queryset(self):
        queryset = Favorite.objects.all().filter(Q(user=self.request.user))
        favorite_articles = []
        for favorite in queryset:
            article = get_object_or_404(Article, slug=favorite.article.slug)
            favorite_articles.append(article)
        return favorite_articles

    def get_serializer_class(self):
        return ArticleListSerializer