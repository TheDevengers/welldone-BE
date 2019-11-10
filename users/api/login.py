from django.contrib.auth import authenticate, login as django_login
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from main.authentication.tokengeneration import TokenGeneration


class ApiLoginHandler(APIView):

    allowed_methods = ['get', 'post', 'put', 'delete', 'options']

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        token = TokenGeneration.generateToken(user_id=user.id, email=user.email)
        django_login(request, user)

        if user:
            content = dict(
                sessionid=request.session.session_key,
                access=token,
                username=user.username,
                id=user.id
            )
        else:
            content = {}

        return Response(data=content, status=status.HTTP_200_OK)
