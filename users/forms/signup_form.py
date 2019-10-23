from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import Profile

class SignupForm(UserCreationForm):
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")
    email = forms.EmailField(label="e-mail")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.email = self.cleaned_data.get("email")
        if commit:
            user.save()
            Profile.objects.create(user=user)
        return user


class ExtendedUserPropertiesForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['description', 'birth_place', 'birth_date', 'user']
