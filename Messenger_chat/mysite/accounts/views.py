from django.shortcuts import render

from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SignUpForm
from chat.models import Profile


class SignUp(CreateView):
    model = Profile
    form_class = SignUpForm
    success_url = '/chat'
    template_name = 'registration/signup.html'
# Create your views here.
