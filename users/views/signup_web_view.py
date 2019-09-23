from django.shortcuts import render, redirect
from django.views import View


from users.forms import SignupForm, ExtendedUserPropertiesForm
from users.controllers import SignupController


class Signup(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('latest_articles')
        form = SignupForm()
        context = dict(
            form=form,
        )
        return render(request, 'users/signup.html', context)
    
    def post(self, request):
        result, data = SignupController.create_new_user(request=request)
        if result:
            return redirect('latest_articles')
        else:
            return render(request, 'users/signup.html', data)
