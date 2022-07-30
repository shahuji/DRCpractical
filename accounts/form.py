from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model

__all__ = ['RegistrationForm', 'ImageUploadForm']

from accounts.models import Images

User = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("name", "username", "email",)
