from django import forms
from twitteruser.models import MyUser


class SignupForm(forms.Form):
    username = forms.CharField(max_length=80)
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)
