from rest_framework.generics import CreateAPIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.contrib.auth import get_user_model

from users.serializers import UserSignUpSerializer, UserSerializer, UserListSerializer

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
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many = True)
        return Response(serializer.data)


class UserAPI(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            updated_user = serializer.save()
            user_serializer = UserSerializer(updated_user)
            return Response(user_serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)