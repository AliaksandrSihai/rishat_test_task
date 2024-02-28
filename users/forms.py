from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
)

from shop.forms import StyleFormMixin
from users.models import User


class UserLogInForm(StyleFormMixin, AuthenticationForm):
    """Стилизация входа"""

    pass


class UserForm(StyleFormMixin, UserCreationForm):
    """Форма для пользователя"""

    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class ProfileForm(StyleFormMixin, UserChangeForm):
    """Форма для профиля пользователя"""

    class Meta:
        model = User
        fields = ("phone", "email", "password", "city", "avatar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget = forms.HiddenInput()
