from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.contrib.auth import get_user_model

from users.serializers import UserSignUpSerializer

User = get_user_model()


class UsersAPI(CreateAPIView):

    serializer_class = UserSignUpSerializer

    def post(self, request, *args, **kwargs):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        username = request.data.get('username')

        if not first_name or not last_name or not email or not username:
            return Response({'detail': 'All The Fields Are Required'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserSignUpSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                # user.set_password
                return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserAPI(APIView):
  def get(self, request, pk):
    return Response()

  def put(self, request, pk):
    return Response()

  def delete(self, request, pk):
    return Response()