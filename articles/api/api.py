from django.db.models import Q
from rest_framework.generics import ListCreateAPIView

from articles.models import Category, Article
from articles.permissions import ArticlePermission
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


class ArticleAPI(APIView):
    def get(self, request, pk):
        return Response()

    def put(self, request, pk):
        return Response()

    def delete(self, request, pk):
        return Response()


class CategoriesAPI(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
