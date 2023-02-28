from django.db import models
#  в модуле аутентификации все же есть базовая форма,
#  позволяющая создать пользователя (в ней реализованы все валидации и проверки)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label='email')
    first_name = forms.CharField(label='Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
