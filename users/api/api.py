from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model
from users.permissions import  UserPermission
from users.serializers import UserSignUpSerializer, UserSerializer, UserListSerializer

User = get_user_model()


class UsersAPI(ListCreateAPIView):
    queryset = User.objects.all()

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

    def get_serializer_class(self):
        return UserListSerializer if self.request.method == 'GET' else UserSignUpSerializer


class UserAPI(RetrieveUpdateDestroyAPIView):

    permission_classes = [UserPermission]

    queryset = User.objects.all()
    serializer_class = UserSerializer
