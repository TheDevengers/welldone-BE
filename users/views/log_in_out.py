from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout as django_logout, login as django_login, authenticate
from django.contrib import messages

from users.forms import LoginForm

class Login(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('latest_articles')

        form = LoginForm()

        context = {'form': form}
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
                django_login(request, user)
                return redirect('latest_articles')
        context = {'form': form}
        return render(request, 'users/login.html', context)

class Logout(View):

    def get(self, request):
        django_logout(request)
        return redirect('latest_articles')
