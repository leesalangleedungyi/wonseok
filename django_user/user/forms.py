from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):

    # password1, 2 부모로부터 상속

    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ['username','email']