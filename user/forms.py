from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', required=True)
    email = forms.EmailField(label='Email', required=True)
    # password = forms.PasswordInput()
    first_name = forms.CharField(label='First Name',)
    last_name = forms.CharField(label='Last Name', )

    class Meta:
        model = User
        fields: tuple = 'username', 'email', 'first_name', 'last_name', 'password1', 'password2'

