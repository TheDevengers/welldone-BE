import jwt
import environ
from django.shortcuts import render, redirect, resolve_url
from django.views import View
from django.contrib.auth import logout as django_logout, login as django_login, authenticate
from django.contrib import messages
from users.forms import LoginForm
from main.authentication.tokengeneration import TokenGeneration

env = environ.Env()
environ.Env.read_env()


class Login(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('latest_articles')

        form = LoginForm()

        context = dict(
            form=form,
            pwd_reset=resolve_url('password_reset_url')
        )

        return render(request, 'users/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'usuario o contraseña incorrectos')
            else:
                token = TokenGeneration.generateToken(user_id=user.id, email=user.email)
                """payload = dict(
                    id=user.id,
                    email=user.email
                )
                token = jwt.encode(payload, env('SECRET_KEY'), 'HS256').decode('utf-8')
                test = jwt.decode(token, env('SECRET_KEY'), 'HS256')"""
                django_login(request, user)
                target = redirect('latest_articles')
                target.set_cookie(key='accessKey', value=token)
                target.set_cookie(key='id', value=user.id)
                target.set_cookie(key='username', value=user.username)
                return target
        context = {'form': form}
        return render(request, 'users/login.html', context)


class Logout(View):

    def get(self, request):
        django_logout(request)
        target = redirect('latest_articles')
        target.delete_cookie(key='accessKey')
        target.delete_cookie(key='id')
        target.delete_cookie(key='username')
        return target
