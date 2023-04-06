from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignupForm(UserCreationForm):

    class Meta:
        # django의 User를 사용한다.
        model = User
        # 사용할 필드는 username, email
        fields = ['username', 'email']
