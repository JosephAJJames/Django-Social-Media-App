from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['email', 'username']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['profilepic', 'email', 'username', 'password']