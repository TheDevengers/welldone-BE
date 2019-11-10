import jwt
from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
import environ

env = environ.Env()
environ.Env.read_env()

class TokenAuthentication(BaseAuthentication):

    model = None

    def get_user(self):
        return User

    def authenticate(self, request):
        try:
            header = self._get_header(request)
            if header is None:
                return None

            user_id = header.get('user_id')

            user = User.objects.get(id=user_id)
            return user, None

        except Exception as e:
            print(e)

    def _get_header(self, request):
        header = request.META.get('HTTP_AUTHORIZATION', b'')
        raw_token = self._get_raw_token(header)

        if raw_token is None:
            return None
        decode = jwt.decode(jwt=raw_token, key=env('SECRET_KEY'))

        return decode

    def _get_raw_token(self, header):

        parts = header.split()
        return parts[1]

    def authenticate_credentials(self, token):
        pass

    def authenticate_header(self, request):
        pass