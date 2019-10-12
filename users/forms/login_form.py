from django import forms


class LoginForm(forms.Form):
    usr = forms.CharField(label="Username")
    pwd = forms.CharField(label='Password', widget=forms.PasswordInput())
