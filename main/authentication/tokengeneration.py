import environ
import jwt

env = environ.Env()
environ.Env.read_env()

class TokenGeneration():

    @staticmethod
    def generateToken(user_id, email):

        payload = dict(
            user_id=user_id,
            email=email
        )

        token = jwt.encode(payload, env('SECRET_KEY'), 'HS256').decode('utf-8')

        return token

