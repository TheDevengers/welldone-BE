from django.contrib.auth import login as django_login

from users.forms import SignupForm


class SignupController(object):

    @staticmethod
    def create_new_user(request):

        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            django_login(request, user)
            return True, 'latest_articles'
        context = {'form': form}
        return False, context

