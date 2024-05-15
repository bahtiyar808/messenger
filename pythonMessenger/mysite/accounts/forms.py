from django import forms
from django.contrib.auth.forms import UserCreationForm
from chat.models import Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = (
            "username",
            "profile_pic",
            "password1",
            "password2",
        )