from django import forms
from django.forms import fields,ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username', 'password1', 'password2']
