from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm (UserCreationForm):
    first_name = forms.CharField(
        max_length=255, min_length=2, required=True, empty_value=False)
    last_name = forms.CharField(
        max_length=255, min_length=2, required=True, empty_value=False)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2"
        )
