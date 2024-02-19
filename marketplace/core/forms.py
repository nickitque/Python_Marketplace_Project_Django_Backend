from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from betterforms.multiform import MultiModelForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ваш никнейм',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email адрес',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Пароль',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Повторите пароль',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

    # phone_code = forms.CharField(widget=forms.PasswordInput(attrs={
    #     'placeholder': 'sss',
    #     'class': 'w-full py-4 px-6 rounded-xl',
    # }))


class AddUserMultiForm(MultiModelForm):
    form_classes = {
        'user': UserCreationForm,
        'profile': SignUpForm,
    }
