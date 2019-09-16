from django.contrib.auth.models import User
from articles.models import Category
from articles.serializers import CategorySerializer, ArticleSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class ArticlesAPI(APIView):
  def post(self, request):
    serializer = ArticleSerializer(data=request.data)

    if serializer.is_valid():
      # TODO Recibir id del autor de la peticion no a través de un parametro
      author = User.objects.get(id=request.data['user_id'])
      new_article = serializer.save(author=author)
      article_serializer = ArticleSerializer(new_article)
      return Response(article_serializer.data, status=status.HTTP_201_CREATED)
    else:
      print(serializer.errors)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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