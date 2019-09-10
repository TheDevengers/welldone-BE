from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView

class UsersAPI(APIView):
  def post(self, request):
    return Response()

class UserAPI(APIView):
  def get(self, request, pk):
    return Response()

  def put(self, request, pk):
    return Response()

  def delete(self, request, pk):
    return Response()