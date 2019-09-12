from django.shortcuts import render, redirect
from django.views import View


class Singup(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('latest_articles')
        form = SignupForm()
        context = {'form': form}
        return render(request, 'users/login.html', context)
