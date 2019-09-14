from django.contrib.auth.models import User
from articles.models.category import Category
from articles.serializers.serializer import CategorySerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class ArticlesAPI(APIView):
  def post(self, request):
    return Response()

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