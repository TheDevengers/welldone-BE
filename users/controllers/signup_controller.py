from django.contrib.auth import login as django_login

from users.forms import SignupForm, ExtendedUserPropertiesForm


class SignupController(object):

    @staticmethod
    def create_new_user(request):

        form = SignupForm(request.POST)
        form2 = ExtendedUserPropertiesForm(request.POST)
        if form.is_valid():
            if form2.is_valid():
                user = form.save()
                form2['user'] = user.pk
                form2.save()
                django_login(request, user)
                return True, 'latest_articles'
        context = dict(
            form=form,
            form2=form2
        )
        return False, context

