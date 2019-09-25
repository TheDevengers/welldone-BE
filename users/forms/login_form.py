from django import forms


class LoginForm(forms.Form):
    usr = forms.CharField(label="username")
    pwd = forms.CharField(label='password', widget=forms.PasswordInput())
