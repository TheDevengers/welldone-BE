from django.shortcuts import render
from django.views import View


class Singup(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = SignupForm()
        context = {'form': form}
        return render(request, 'users/login.html', context)
